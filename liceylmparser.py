from bs4 import BeautifulSoup
from tqdm.auto import tqdm
from pathlib import Path
import argparse
import requests
import zipfile
import shutil as poshutil
import pickle
import os
import re



def load_session(cookie_file='cookies.pkl'):
    session = requests.Session()
    with open(cookie_file, 'rb') as f:
        cookies_data = pickle.load(f)
    if isinstance(cookies_data, list):
        jar = requests.cookies.RequestsCookieJar()
        for cookie_dict in cookies_data:
            name = cookie_dict.get('name')
            value = cookie_dict.get('value')
            domain = cookie_dict.get('domain', '')
            path = cookie_dict.get('path', '/')
            secure = cookie_dict.get('secure', False)
            rest = cookie_dict.get('rest', {})
            if name and value is not None:
                jar.set(name, value, domain=domain, path=path, secure=secure, **rest)
        session.cookies = jar
    elif isinstance(cookies_data, dict):
        session.cookies.update(cookies_data)
    else:
        session.cookies = cookies_data
    return session


def fetch_tasks(session, course_id, group_id):
    url = 'https://lms.yandex.ru/api/student/tasks'
    params = {
        'courseId': course_id,
        'groupId': group_id,
        'excludeAccepted': 'false',
        'excludeExpired': 'false',
        'order': 'deadline'
    }
    resp = session.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data.get('results', [])


def fetch_task(session, task_id, group_id):
    url = f'https://lms.yandex.ru/api/student/tasks/{task_id}'
    params = {'groupId': group_id}
    resp = session.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


def fetch_solution(session, solution_id, course_id, group_id):
    url = f'https://lms.yandex.ru/api/student/solutions/{solution_id}'
    params = {
        'courseId': course_id,
        'groupId': group_id
    }
    resp = session.get(url, params=params)
    resp.raise_for_status()
    return resp.json()["solution"]


def download_file(session, file_url, local_file):
    resp = session.get(file_url)
    resp.raise_for_status()
    local_file.write_bytes(resp.content)
    if str(local_file).endswith('.zip'):
        extract_to = os.path.dirname(local_file)
        with zipfile.ZipFile(local_file, 'r') as zip_ref:
            members = zip_ref.namelist()
            if len(members) == 1 and members[0].endswith('/'):
                inner_folder = members[0]
                temp_extract = os.path.join(extract_to, '_temp_extract')
                zip_ref.extractall(temp_extract)
                src_folder = os.path.join(temp_extract, inner_folder)
                for item in os.listdir(src_folder):
                    src_path = os.path.join(src_folder, item)
                    dst_path = os.path.join(extract_to, item)
                    poshutil.move(src_path, dst_path)
                poshutil.rmtree(temp_extract)
                os.remove(local_file)
            else:
                zip_ref.extractall(extract_to)
                os.remove(local_file)



def sanitize_path_component(name):
    forbidden = r'<>:"/\|?*'
    for ch in forbidden:
        name = name.replace(ch, '_')
    return name.strip().rstrip('.')


def html_to_markdown(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, 'html.parser')

    def process(elem):
        if elem.name is None:
            return elem.string or ""

        if elem.name == 'pre':
            return f"\n```\n{elem.get_text().strip()}\n```\n"
        if elem.name == 'code':
            return f"`{elem.get_text().strip()}`"
        if elem.name in ('strong', 'b'):
            return f"**{''.join(process(ch) for ch in elem.children)}**"
        if elem.name in ('em', 'i'):
            return f"*{''.join(process(ch) for ch in elem.children)}*"
        if elem.name == 'a':
            href = elem.get('href', '')
            inner = ''.join(process(ch) for ch in elem.children)
            return f"[{inner}]({href})"
        if elem.name == 'br':
            return "\n"
        if elem.name == 'p':
            inner = ''.join(process(ch) for ch in elem.children)
            return f"\n{inner.strip()}\n"
        if elem.name in ('ul', 'ol'):
            items = []
            for li in elem.find_all('li', recursive=False):
                li_text = ''.join(process(ch) for ch in li.children)
                items.append(f"- {li_text.strip()}")
            return "\n" + "\n".join(items) + "\n"
        return ''.join(process(ch) for ch in elem.children)

    result = process(soup)
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = re.sub(r'[ \t]+\n', '\n', result)
    return result.strip()


def extract_task_from_html(html_desc):
    soup = BeautifulSoup(html_desc, 'html.parser')

    time_limit = memory_limit = None
    time_td = soup.find('td', string='Ограничение времени')
    if time_td:
        time_limit = time_td.find_next_sibling('td').get_text(strip=True)
    mem_td = soup.find('td', string='Ограничение памяти')
    if mem_td:
        memory_limit = mem_td.find_next_sibling('td').get_text(strip=True)

    legend = soup.find('div', class_='legend')
    description = html_to_markdown(str(legend)) if legend else ""

    input_spec = soup.find('div', class_='input-specification')
    input_text = html_to_markdown(str(input_spec)) if input_spec else ""
    output_spec = soup.find('div', class_='output-specification')
    output_text = html_to_markdown(str(output_spec)) if output_spec else ""

    samples = []
    sample_table = soup.find('table', class_='sample-tests')
    if sample_table:
        pres = sample_table.find_all('pre')
        for i in range(0, len(pres) - 1, 2):
            inp = pres[i].get_text(strip=False).strip()
            out = pres[i+1].get_text(strip=False).strip()
            samples.append((inp, out))

    notes_div = soup.find('div', class_='notes')
    notes_text = html_to_markdown(str(notes_div)) if notes_div else ""

    return {
        'time_limit': time_limit,
        'memory_limit': memory_limit,
        'description': description,
        'input_format': input_text,
        'output_format': output_text,
        'samples': samples,
        'notes': notes_text
    }


def save_readme(dir_path: Path, task_info: dict, solution_info: dict):
    lines = [f"# {task_info.get('title', 'Без названия')}\n"]

    html_desc = task_info.get('description', '')
    if html_desc:
        sec = extract_task_from_html(html_desc)
        if sec['time_limit']:
            lines.append(f"**Ограничение времени:** {sec['time_limit']}")
        if sec['memory_limit']:
            lines.append(f"**Ограничение памяти:** {sec['memory_limit']}")
        lines.append("")
        if sec['description']:
            lines.append(sec['description'])
            lines.append("")
        if sec['input_format']:
            lines.append("## Формат ввода")
            lines.append(sec['input_format'])
            lines.append("")
        if sec['output_format']:
            lines.append("## Формат вывода")
            lines.append(sec['output_format'])
            lines.append("")
        if sec['samples']:
            lines.append("## Примеры")
            for idx, (inp, out) in enumerate(sec['samples'], 1):
                lines.append(f"### Пример {idx}")
                lines.append("**Ввод:**")
                lines.append(f"```\n{inp}\n```")
                lines.append("**Вывод:**")
                lines.append(f"```\n{out}\n```")
            lines.append("")
        if sec['notes']:
            lines.append("## Примечания")
            lines.append(sec['notes'])
            lines.append("")

    lines.append("---")
    lines.append("## Информация о решении\n")
    lines.append(f"**Урок:** {task_info.get('lesson', {}).get('title', '—')}  ")
    lines.append(f"**Максимальный балл:** {task_info.get('scoreMax', '—')}  ")
    lines.append(f"**Полученный балл:** {solution_info.get('score', '—')}  ")

    status = solution_info.get('status', {}).get('type')
    if not status and 'latestSubmission' in task_info:
        status = "Решено" if task_info['latestSubmission'].get('verdict') == 'ok' else task_info['latestSubmission'].get('verdict')
    lines.append(f"**Статус:** {status or '—'}  ")

    date_str = solution_info.get('updateTime') or task_info.get('latestSubmission', {}).get('addedTime', '—')
    lines.append(f"**Дата:** {date_str}  ")

    sub = solution_info.get('latestSubmission') or task_info.get('latestSubmission')
    if sub:
        lines.append(f"**Контест:** {sub.get('contestId', '—')}  ")
        lines.append(f"**Вердикт:** {sub.get('verdict', '—')}  ")

    readme_path = dir_path / 'readme.md'
    readme_path.write_text('\n'.join(lines), encoding='utf-8')



def main():
    parser = argparse.ArgumentParser(description="Парсер задач LMS Яндекса")
    parser.add_argument("course_id", help="ID курса")
    parser.add_argument("group_id", help="ID вашей группы")
    parser.add_argument("--cookies", "-c", dest="cookies_path", default="cookies.pkl",
                        help="Путь к файлу с cookies (по умолчанию cookies.pkl)")
    parser.add_argument("--output", "-o", dest="output_dir", default="LMParserData",
                        help="Папка для сохранения данных (по умолчанию LMParserData)")

    args = parser.parse_args()
    course_id = args.course_id
    group_id = args.group_id
    cookies_path = Path(args.cookies_path)
    base_dir = Path.cwd() / args.output_dir
    base_dir.mkdir(exist_ok=True)

    session = load_session(cookies_path)
    tasks = fetch_tasks(session, course_id, group_id)
    print(f"Найдено задач: {len(tasks)}")

    for task in tqdm(tasks, desc="Обработка задач", unit="task"):
        solution_info = task.get('solution')
        if not solution_info:
            continue
        solution_id = solution_info['id']
        tqdm.write(f"Обрабатываем решение {solution_id} для задачи {task.get('title')}")

        try:
            solution_data = fetch_solution(session, solution_id, course_id, group_id)
        except Exception as e:
            tqdm.write(f"  Ошибка загрузки решения {solution_id}: {e}")
            continue
        try:
            task_data = fetch_task(session, task["id"], group_id)
        except Exception:
            task_data = solution_data.get('task', {})

        lesson_dir = sanitize_path_component(task_data.get('lesson', {}).get('title', 'Без урока'))
        task_dir = sanitize_path_component(task_data.get('title', 'Без названия'))
        target_dir = base_dir / str(course_id) / lesson_dir / task_dir
        target_dir.mkdir(parents=True, exist_ok=True)

        if (target_dir / 'readme.md').exists():
            try:
                content = (target_dir / 'readme.md').read_text(encoding='utf-8')
                if "**Статус:** accepted" in content:
                    tqdm.write(f"  Пропускаем {task.get('title', 'Без названия')} (уже решена)")
                    continue
            except Exception: pass

        save_readme(target_dir, task_data, solution_data)

        latest_sub = solution_data.get('latestSubmission')
        if latest_sub and latest_sub.get('file'):
            try:
                download_file(session, latest_sub['file']['url'],
                              target_dir / latest_sub['file'].get('name', 'solution.py'))
            except Exception as e:
                tqdm.write(f"  Ошибка скачивания файла: {e}")
        else:
            source_code = latest_sub.get('sourceCode') if latest_sub else None
            if source_code:
                (target_dir / 'solution.py').write_text(source_code, encoding='utf-8')
                tqdm.write(f"  solution.py сохранён из sourceCode")
            else:
                tqdm.write(f"  Нет файла решения для задачи {solution_id}")

    print("Готово.")



if __name__ == '__main__':
    main()
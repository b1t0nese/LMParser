from undetected_chromedriver import Chrome
import argparse
import pickle
import os

parser = argparse.ArgumentParser(
    description="Автоматическое получение cookies для указанного сайта через undetected_chromedriver")
parser.add_argument("url", help="URL сайта, который будет открыт")
parser.add_argument("--cookies", "-c", dest="cookies_path", default=None,
                    help="Путь к файлу для сохранения/чтения cookies (по умолчанию: cookies.pkl в папке скрипта)")
parser.add_argument("--version", "-v", type=int, dest="version_main", default=None,
                    help="Основная версия Chrome (например, 148). Если не указана, будет определена автоматически.")
args = parser.parse_args()

driver_kwargs = {}
if args.version_main:
    driver_kwargs["version_main"] = args.version_main
driver = Chrome(**driver_kwargs)
driver.get(args.url)

cookies_path = os.path.join(os.path.dirname(__file__), "cookies.pkl") if args.cookies_path is None else cookies_path = args.cookies_path
if not os.path.exists(cookies_path):
    print(f'Файл cookies по пути "{cookies_path}" не найден.')
    input("Пожалуйста, войдите в аккаунт и нажмите Enter: ")
    cookies = driver.get_cookies()
    with open(cookies_path, "wb") as f:
        pickle.dump(cookies, f)
    print(f"Cookies сохранены в {cookies_path}")
else:
    print(f"Файл cookies уже существует: {cookies_path}")

input("Нажмите Enter для закрытия браузера...")
driver.quit()
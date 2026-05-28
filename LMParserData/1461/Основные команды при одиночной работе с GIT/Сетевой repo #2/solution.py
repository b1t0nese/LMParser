mkdir -p git_lab1_lesson2
cd git_lab1_lesson2

git clone https://github.com/YandexLyceum/human.git
cd human

echo "=== Все ветки (локальные и удалённые) ==="
git branch -a
echo "=== Содержимое файла human.txt ==="
cat human.txt

echo "=== Сравнение master с boots ==="
git --no-pager diff origin/master origin/boots -- human.txt
echo "=== Сравнение master с buttons ==="
git --no-pager diff origin/master origin/buttons -- human.txt
echo "=== Сравнение master с demo ==="
git --no-pager diff origin/master origin/demo -- human.txt
echo "=== Сравнение master с hat ==="
git --no-pager diff origin/master origin/hat -- human.txt

git checkout -b boots_buttons master
echo "=== Мерджим origin/boots origin/buttons в boots_buttons ==="
git merge origin/boots -m "merge origin/boots into boots_buttons"
git merge origin/buttons -m "merge origin/buttons into boots_buttons"
echo "Изменения в файле human.txt, принесённые ветками boots и buttons, затрагивают разные строки, поэтому Git смог объединить их автоматически. Поэтому, конфликтов при слиянии веток boots и buttons в boots_buttons не возникло."

git checkout master

echo "=== Мерджим origin/hat и boots_buttons в master ==="
git merge origin/hat -m "merge origin/hat into master"
git merge boots_buttons -m "merge boots_buttons into master"

echo "=== Сравнение master и origin/demo ==="
git --no-pager diff master origin/demo
echo 'Отличие заключается в том, что в README убирается "with nice buttons on his jacket (buttons branch)".'

echo "=== Добавляем удалённый репозиторий student и добавляем туда master ==="
git remote add student https://git@git.sourcecraft.dev/h0rnid/human.git
git push -u student master
git fetch student
echo "=== Информация о коммитах в student/master ==="
git --no-pager log student/master --oneline

read -p "Нажмите Enter для выхода..."
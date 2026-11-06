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

read -p "Нажмите Enter для выхода..."
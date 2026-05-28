mkdir git_repo_2
cd git_repo_2
git init
echo -e "4\r\n5\r\n6\r\n7" > numbers.txt
git add numbers.txt
git commit -m "add numbers.txt"
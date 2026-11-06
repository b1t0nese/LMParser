mkdir git_repo_2
cd git_repo_2
git init
echo -e "4\r\n5\r\n6\r\n7" > numbers.txt
git add numbers.txt
git commit -m "add numbers.txt"
git checkout --orphan branch1234567
echo -e "1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7" > numbers.txt
git add numbers.txt
git commit -m "create branch1234567 and add file"
git checkout master
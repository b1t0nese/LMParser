mkdir git_repo_2
cd git_repo_2
git init
echo -e "4\r\n5\r\n6\r\n7" > numbers.txt
git add numbers.txt
git commit -m "add numbers.txt"
git checkout -b branch1234567
echo -e "1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7" > numbers.txt
git add numbers.txt
git commit -m "create branch1234567 and add file"
git checkout master
git branch branch4567890
git checkout branch4567890
echo -e "4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n0" > numbers.txt
git add numbers.txt
git commit -m "create branch4567890 and add file"
git checkout master
git merge branch1234567 -m "merge branch1234567"
git merge branch4567890 -m "merge branch4567890"
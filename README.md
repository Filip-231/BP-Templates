# Boilerplate


```
git clone git@github.com:Filip-231/Boilerplate
git filter-branch --index-filter 'git rm --ignore-unmatch --cached -qr -- . && git reset -q $GIT_COMMIT -- templates/ ' --prune-empty -- --all
git remote rm origin
mkdir ~/Desktop/New-project
mv * ~/Desktop/New-project
mv .git ~/Desktop/New-project
cd ~/Desktop/New-project
git remote add origin git@github.com:Filip-231/BP-Test.git
git pull origin master --allow-unrelated-histories
git push origin master
```










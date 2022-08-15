# Init
This repository is made to initialize new projects with all design patterns included. All You need to do is:
```
git clone git@github.com:Filip-231/Init.git abc-test && cd abc-test && make git _PROJECT=abc-test _USER=Filip-231 && make init && make all
```
Fill **_PROJECT** with a name of you new project, and **_USER** with the name of your Github user.

To have access to all make commands You need to create venv:

```make install```

And You are good to go! Isn't this genius?

To configure pytest in Pycharm add: ```-p no:allure_pytest_bdd``` to additional parameters.

### Useful not necessary commands:

- Can be used for filtering git repo if you want to delete some files:

```git filter-branch --index-filter 'git rm --ignore-unmatch --cached -qr -- . && git reset -q $GIT_COMMIT -- . ' --prune-empty -- --all```


- Can be used for pulling when repo is not empty:

``git pull origin master --allow-unrelated-histories``

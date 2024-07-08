# Syncing the downstream fork from the upstream repository

Using the UI there is a "Sync fork" button, that works, if there are no conflicts.

There is also a cli tool "gh" which can be used, see
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork

But this only works, if there are no conflicts

## handling conflicts

https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github

### Add the remote, call it "upstream":

```
git remote add upstream https://github.com/tmforum-oda/oda-canvas.git
git remote set-url --push upstream https://no-push-to-upstream-allowed

git remote -v
```


### Fetch all the branches of that remote into remote-tracking branches

```
git fetch upstream
```

### Make sure that you're on your master branch:

```
git checkout master
git pull
```

### Update master branch

Rewrite your master branch so that any commits of yours that
aren't already in upstream/master are replayed on top of that
other branch:

```
#git rebase upstream/master
git merge upstream/master

# to automate define preference of upstream changes with -Xtheirs
#git merge -Xtheirs upstream/master
```

## configure username and email

```
$ git config credential."https://github\.com".username john-doe
$ git config credential."https://github\.com".email john.doe@invalid.domain
```

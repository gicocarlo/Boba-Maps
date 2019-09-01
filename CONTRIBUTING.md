# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off from the creator of the repository, or if you 
   do not have permission to do that, you may request the creator to merge it for you.

## Beginners Guide to Pull Requests

1. Make a remote and local branch (local branch below)
```
$ git checkout -b <branch name>
```

2. Once you've finished making changes: add & commit
```
$ git add <files you want to add>
$ git commit -m <commit message>
```

3. Finally make a pull request
```
$ git push origin head
```

## Updating Fork
To make sure your fork is up-to-date, do the following:

1. Do the following if you haven't cloned your remote repo to your local machine (If you have skip to step 2):
```
$ git clone https://github.com/[Username]/Boba-Maps.git
```

2. If you haven't made an upstream, do the following:
```
$ cd <your/local/cloned/repo/path/here>
$ git remote add upstream https://github.com/RiceAbove/Boba-Maps.git
```

3. Now fetch upstream:
```
$ git fetch upstream
$ git rebase upstream/master
```

4. Finally push to your fork
```
$ git push -f origin master
```


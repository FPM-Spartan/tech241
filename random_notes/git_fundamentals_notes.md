# GIT FUNDAMENTALS TEACHABLE NOTES

* What is VC?
* What is git?
* Installation on windows
* creating a git repo
* staging and committing files in git
* creating a github account
* copying a local repo to github
* copying a github repo locally
* syncing locsal and remote repo copies
* what's next?

## What is VC?

Version Control is for anyone who creates content:
* remembers each version update
* provides a history of all changes
* can go bac to an earlier version

Can provide off-site copy of data
* easy sync with local copy

Supports collaboration
* people might update simultaneously
* might make overlappping changes
* can support merging and dealing with conflicts

## What is git?

* git is a version control system.
* fast, modern, fully featured. 
* by far the most popular vcs
* open source and free
* provides version history
* great for collab work
* distributed
  * local copy
  * optional remote copy

### What is provided with git?

* command line usr interface called git Bash
  * all commands can be run through this UI
* git server can be used to copy data
  * included with git
  * most people use an internet solution
  * popular options include github, gitlab, bitbucket
* GUI can also be used
  * github desktop and IDE integration
* directory/folder controlled by git is called a REPOSITORY (repo)

## Installing Git

git-scm.com/downloads

select file location (or leave default)

associate .sh files to be run with Bash

associate git files with default text editor

change default editor from Vim to notepad

better to have main as the main branch name instead of master (master is starting to be phased out as the terminology)

everything else should be fine

**install**

### Single Branch Git

start -> first version -> experiment -> tests (revert back if unsuccessful, and experiment and test versions will be erased)

### multi branch git
                      / Experiment -> tests !=0 experiment branch
start -> first version -> main branch

### create a git repo

* git init
  * run in the folder you want to have controlled by git
  * this creates a subfolder called .git, that stores config info, remembers version history for all files in folder, all branches, keeps track of current working (HEAD)
* can create .gitignore
  * exclude certain files from git control
  * easy to create via templates on github

### Staging and Committing
working directory -> git add -> staging area -> git commit -> local repo -> git push -> push that commit to the connected repo on github

Adding files to the index is the same as staging, just different terminology.
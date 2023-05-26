
amiran@DESKTOP-M1RAP7G MINGW64 ~
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

amiran@DESKTOP-M1RAP7G MINGW64 ~
$

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ git config --global user.name mjavadpur

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ git config --global user.email mjavadpur@gmail.com

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ pwd
/c/Users/amiran

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ mkdir FirstGitPrj

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ cd FirstGitPrj/

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj
$ GIT INIT
git: 'INIT' is not a git command. See 'git --help'.

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj
$ git init
Initialized empty Git repository in C:/Users/amiran/FirstGitPrj/.git/

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ touch Hangman.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Hangman.ipynb

nothing added to commit but untracked files present (use "git add" to track)

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git add hangman.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git add .

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git commit -m "These are my first git operations"
[master (root-commit) bfe85dc] These are my first git operations
 2 files changed, 2 insertions(+)
 create mode 100644 Hangman.ipynb
 create mode 100644 Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log
commit bfe85dcc7a8a2d5379f87f4bd13736ddf3f9da58 (HEAD -> master)
Author: mjavadpur <mjavadpur@gmail.com>
Date:   Fri May 26 17:14:38 2023 +0330

    These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log --online
fatal: unrecognized argument: --online

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log --oneline
bfe85dc (HEAD -> master) These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git restor --stage hangman.ipynb
git: 'restor' is not a git command. See 'git --help'.

The most similar commands are
        restore
        remote

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git restore --stage hangman.ipynb
error: pathspec 'hangman.ipynb' did not match any file(s) known to git

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git restore --stage Hangman.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log
commit bfe85dcc7a8a2d5379f87f4bd13736ddf3f9da58 (HEAD -> master)
Author: mjavadpur <mjavadpur@gmail.com>
Date:   Fri May 26 17:14:38 2023 +0330

    These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git restore --stage Hangman.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git restore --stage Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git branch
* master

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git branch amin

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git branch
  amin
* master

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git switch amin
Switched to branch 'amin'

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git branch
* amin
  master

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ touch SAM.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git add .

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git status
On branch amin
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   SAM.ipynb


amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git commit -m "Commit sam file"
[amin da7e623] Commit sam file
 1 file changed, 1 insertion(+)
 create mode 100644 SAM.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git status --oneline
error: unknown option `oneline'
usage: git status [<options>] [--] [<pathspec>...]

    -v, --verbose         be verbose
    -s, --short           show status concisely
    -b, --branch          show branch information
    --show-stash          show stash information
    --ahead-behind        compute full ahead/behind values
    --porcelain[=<version>]
                          machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)
    --ignored[=<mode>]    show ignored files, optional modes: traditional, matching, no. (Default: traditional)
    --ignore-submodules[=<when>]
                          ignore changes to submodules, optional when: all, dirty, untracked. (Default: all)
    --column[=<style>]    list untracked files in columns
    --no-renames          do not detect renames
    -M, --find-renames[=<n>]
                          detect renames, optionally set similarity index


amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git log --oneline
da7e623 (HEAD -> amin) Commit sam file
bfe85dc (master) These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (amin)
$ git switch master
Switched to branch 'master'

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git merge amin
Updating bfe85dc..da7e623
Fast-forward
 SAM.ipynb | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 SAM.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ ls
Hangman.ipynb  SAM.ipynb  Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ nano FirstGitPrj.sh

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ 1.sh
bash: 1.sh: command not found

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ FirtGitPrj.sh
bash: FirtGitPrj.sh: command not found

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ FirstGitPrj.sh
bash: FirstGitPrj.sh: command not found

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ nano FirstGitPrj.sh

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ FirstGitPrj.sh
bash: FirstGitPrj.sh: command not found

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ bash FirstGitPrj.sh
Hello Amin !!!

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        FirstGitPrj.sh

nothing added to commit but untracked files present (use "git add" to track)

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git add .
warning: in the working copy of 'FirstGitPrj.sh', LF will be replaced by CRLF the next time Git touches it

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git commit -m "end!!!"
git commit -m "endgit add .!"
[master dcc73ea] endgit add .!
 1 file changed, 1 insertion(+)
 create mode 100644 FirstGitPrj.sh

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git status
On branch master
nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log
commit dcc73eaff840a34ce24703b4a8a1cae4452e5726 (HEAD -> master)
Author: mjavadpur <mjavadpur@gmail.com>
Date:   Fri May 26 18:16:37 2023 +0330

    endgit add .!

commit da7e623faad979cb3558653168f9da93fa399037 (amin)
Author: mjavadpur <mjavadpur@gmail.com>
Date:   Fri May 26 17:45:52 2023 +0330

    Commit sam file

commit bfe85dcc7a8a2d5379f87f4bd13736ddf3f9da58
Author: mjavadpur <mjavadpur@gmail.com>
Date:   Fri May 26 17:14:38 2023 +0330

    These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log oneline
fatal: ambiguous argument 'oneline': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ git log --oneline
dcc73ea (HEAD -> master) endgit add .!
da7e623 (amin) Commit sam file
bfe85dc These are my first git operations

amiran@DESKTOP-M1RAP7G MINGW64 ~/FirstGitPrj (master)
$ cd ..

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ git clone https://github.com/mjavadpur/GitPrj.git
Cloning into 'GitPrj'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=openssl
http.sslcainfo=C:/Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
core.editor="C:\Users\amiran\AppData\Local\Programs\Microsoft VS Code\bin\code" --wait
gui.recentrepo=C:/Users/amiran/Desktop/IntroGit
user.name=mjavadpur
user.email=mjavadpur@gmail.com

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ pwd
/c/Users/amiran

amiran@DESKTOP-M1RAP7G MINGW64 ~
$ cd GitPrj

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj (main)
$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 1), reused 6 (delta 1), pack-reused 0
Unpacking objects: 100% (6/6), 4.66 KiB | 340.00 KiB/s, done.
From https://github.com/mjavadpur/GitPrj
   d419537..63348ae  main       -> origin/main
Updating d419537..63348ae
Fast-forward
 GitPrj/FirstGitProject.ipynb | 1 +
 GitPrj/Hangman.ipynb         | 1 +
 GitPrj/Sudoku.ipynb          | 1 +
 3 files changed, 3 insertions(+)
 create mode 100644 GitPrj/FirstGitProject.ipynb
 create mode 100644 GitPrj/Hangman.ipynb
 create mode 100644 GitPrj/Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj (main)
$ cd
.git/      GitPrj/    LICENSE    README.md

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj (main)
$ cd
.git/      GitPrj/    LICENSE    README.md

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj (main)
$ cd GitPrj/

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ cd
cd              cdosys.dll      cdprt.dll       cdpusersvc.dll
cdd.dll         cdp.dll         cdpsvc.dll

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ cddir
bash: cddir: command not found

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ dir
FirstGitProject.ipynb  Hangman.ipynb  Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ rm Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    Sudoku.ipynb

no changes added to commit (use "git add" and/or "git commit -a")

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git add .

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    Sudoku.ipynb


amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git commit -m "I delete Sudoku.ipynb file"
[main 375db06] I delete Sudoku.ipynb file
 1 file changed, 1 deletion(-)
 delete mode 100644 GitPrj/Sudoku.ipynb

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git log oneline
fatal: ambiguous argument 'oneline': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git log --oneline
375db06 (HEAD -> main) I delete Sudoku.ipynb file
63348ae (origin/main, origin/HEAD) These files commited from my colab!
d419537 Initial commit

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git remote -v
origin  https://github.com/mjavadpur/GitPrj.git (fetch)
origin  https://github.com/mjavadpur/GitPrj.git (push)

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 341 bytes | 341.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/mjavadpur/GitPrj.git
   63348ae..375db06  main -> main

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$ git log --oneline
375db06 (HEAD -> main, origin/main, origin/HEAD) I delete Sudoku.ipynb file
63348ae These files commited from my colab!
d419537 Initial commit

amiran@DESKTOP-M1RAP7G MINGW64 ~/GitPrj/GitPrj (main)
$

# islanddetection
## Installation
**In ubuntu:**

    sudo apt-get install git
    git config --global user.name <your github username>
    git config --global user.email <your github-registered email>

## How to use this repository
**Note:** All of the below instructions are to be executed in command line.

Since I have added you guys as collaborators.

1. Do the following in the directory where you want to download this project. The command will create a folder for you
and will keep all the stuff in it there.
    
    `git clone https://github.com/abhiroyg/islanddetection.git`

1. But if you already have a folder and you have some files you want to push to this repository.

    1. `cd` to that folder.
    1. Do `git init` - this will make the folder git-recognizable.
    1. Do `git remote add origin https://github.com/abhiroyg/islanddetection.git` - this will tell where to push to.
    1. Do `git add .` to add all of the files in your folder. If you don't want to add all of them. Just add one by one.
        
      For example: `git add bases.txt`
    
    1. Do `git commit -m "<some message>"` - generally the message should tell the changes you did briefly.
    1. Do `git push -u origin master`

1. Some of the commands would need you to enter your username/email and password. Enter them.
1. Now, you have the repository setup on your system/laptop/computer/desktop.
1. If you make any changes in the files you added or you created new files or you deleted the files you added.
   Do `git status` and you can see the files that are changed/deleted.
   
   Suppose you deleted files before adding to git. You can be sure to never see that file in your life again.
   But if you add it to git. You can recover it.

1. Now, for the files you added, if you want to see what changes you did. Do `git diff`.
1. If you are sure you want to push these changes into the repository hosted at github. Do

    1. `git add <filename>` (or) `git add <filename> <filename>` (or) `git add <foldername>`
    1. `git commit -m "<some message describing the changes you are about to push>"`
    1. `git push origin master` - note that there is no `-u` now. That is only one-time thing. This is every time thing.

# Git :- Git is a distributed version control system that allows multiple developers to work on a project simultaneously. It tracks changes in source code during software development, enabling collaboration and maintaining a history of modifications. Git is widely used for managing code repositories, facilitating branching and merging, and supporting workflows for continuous integration and deployment.

# Git workflow :
# 1. Working Directory
# 2. Stage
# 3. Local Repository
# 4. Commit

# git init : Initializes a new git repository in the current directory.

# git status : Displays the current status of the working directory and staging area, showing which files have been modified, added, or deleted.

# git add <file> : Adds changes in the specified file(s) to the staging area, preparing them for the next commit.

# git commit -m "commit message" : Records the changes in the staging area to the local repository with a descriptive commit message.

# git log : Shows the commit history of the repository, including commit hashes, authors, dates, and messages.

# track changes

# git ignore : Specifies intentionally untracked files to ignore, preventing them from being included in commits.
# .gitignore : A file that lists patterns for files and directories to be ignored by Git, helping to keep the repository clean and focused on relevant files.

# NOTE : Git doesn't keep the track of empty directories. If you want to keep the empty directory in the repository, you can create a .gitkeep file inside that directory. The .gitkeep file is an empty file that serves as a placeholder, allowing Git to track the otherwise empty directory.

# Branch and Merge : Git allows developers to create branches, which are separate lines of development. Branches enable experimentation and feature development without affecting the main codebase. Merging combines changes from different branches back into a single branch, facilitating collaboration and integration of new features.
# To create a new git branch, you can use the command `git branch <branch-name>`. To switch to a different branch, use `git checkout <branch-name>`. Merging can be done with `git merge <branch-name>`.

# now i'm gonna merge this in my master brach let's see if this reflects there or not first i have to commit this in this branch, and there are dummy files that i have deleted from here let's see if they are there or not 

# to delete branch use : git brnach -d <brach name>

#Stashing : Git provides a feature called "stash" that allows you to temporarily save changes in your working directory without committing them. This is useful when you need to switch branches or work on something else without losing your current changes. You can use `git stash` to save your changes and `git stash apply` to reapply them later.

# git stash list : Lists all the stashed changes in the repository, allowing you to view and manage saved work that is temporarily set aside.

# git stash pop : Applies the most recent stashed changes and removes them from the stash list, effectively restoring your working directory to the state it was in before the stash was created.

# Now everything is done and i'm gonna tag my commit
# git tag -a <tag-name> -m "tag message" : Creates an annotated tag with a specified name and message, allowing you to mark specific points in the commit history for reference. 
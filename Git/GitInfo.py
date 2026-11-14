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
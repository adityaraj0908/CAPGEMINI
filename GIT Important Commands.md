# GIT Important Commands



| **Git Command** | **Explanation** |
| --- | --- |
| `git branch` | Lists all local branches. |
| `git branch sub-branch` | Creates a new branch named `sub-branch`. |
| `git switch branch` | Switches to the specified `branch`. |
| `git switch -c sub-branch` | Creates and switches to `sub-branch`. |
| `git branch sub-branch parent-branch` | Creates `sub-branch` from `parent-branch`. |
| `git switch -c sub-branch parent-branch` | Creates and switches to `sub-branch` from `parent-branch`. |
| `git branch -D sub-branch` | Force deletes the local `sub-branch`. |
| `git push origin --delete sub-branch` | Deletes `sub-branch` from the remote repository. |
| `git branch -r` | Lists all remote branches. |
| `git merge sub-branch` | Merges `sub-branch` into the current branch. |
| `git diff --name-only --diff-filter=U` | Lists files with unresolved merge conflicts. |
| `git status` | Shows the current working state of the repository. |
| `git commit -m "merge commit"` | Commits the merged changes with a message. |
| `git push origin sub-branch` | Pushes `sub-branch` to the remote repository. |
| `git log --merges -1` | Shows the latest merge commit. |
| `git log --oneline --graph --decorate --all` | Displays a visual history of all commits and branches. |
| `git stash` | Stashes uncommitted changes temporarily. |
| `git stash list` | Lists all stashed changes. |
| `git stash pop` | Applies and removes the latest stash. |
| `git stash pop "stash@{0}"` | Applies and removes a specific stash by index. |
| `git stash drop` | Deletes the latest stash. |
| `git stash drop "stash@{0}"` | Deletes a specific stash by index. |
| `git stash clear` | Removes all stashed changes. |
| `git revert HEAD` | Creates a new commit that undoes the latest commit. |
| `git reset --hard HEAD~1` | Resets the last commit **and deletes changes**. |
| `git reset --soft HEAD~1` | Resets the last commit **but keeps changes staged**. |
| `git log --oneline --graph --decorate -n 5` | Shows the last 5 commits in a compact graphical format. |
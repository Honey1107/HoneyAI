# 08 GitHub Workflow
# 1. Commit your Python fundamentals changes
git commit -m "Add Python fundamentals practice"

# 2. Push the feature branch to GitHub
git push -u origin feature/python-practice

# 3. Switch back to the main branch
git checkout main

# 4. Get the latest changes from the remote main branch
git pull origin main

# 5. Delete the local feature branch after the merge is complete
git branch -d feature/python-practice

# 6. Check the current Git status
git status

# 7. Display all local branches
git branch

# 8. Display the last 5 commits
git log --oneline -5

# 9. Display the remote GitHub repository URL
git remote -v


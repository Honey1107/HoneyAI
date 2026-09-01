# 05 Merge
# Switch to main
git checkout main

# Get the merged changes
git pull origin main

# Delete the local feature branch
git branch -d feature/python-practice

# Verify everything is clean
git status

# Check branches
git branch

# Check recent commits
git log --oneline -5

# Check remote repository
git remote -v



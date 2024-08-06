p=$(pwd)
git config --global --add safe.directory $p
git pull origin main

if [[ "$(git status --porcelain)" != "" ]]; then
    git config --global user.name $USERNAME
    git config --global user.email $USER_EMAIL
    git add -A .
    git commit -m "$COMMIT_MESSAGE"
    git push
else
echo "Nothing to commit..."
fi

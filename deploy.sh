#!/bin/bash
# Simple deployment script

echo "🚀 Deploying Jekyll AP Database..."

# Check if there are changes
if git diff --quiet && git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "📝 Committing changes..."
    git add .
    read -p "Enter commit message (or press Enter for default): " commit_msg
    if [ -z "$commit_msg" ]; then
        commit_msg="Update AP database - $(date +'%Y-%m-%d %H:%M')"
    fi
    git commit -m "$commit_msg"
fi

echo "📤 Pushing to GitHub..."
git push origin main

echo "✅ Deployment complete!"
echo "🌐 Your site will be available at: https://USERNAME.github.io/REPOSITORY"
echo "⏱️  GitHub Pages builds usually take 1-2 minutes"

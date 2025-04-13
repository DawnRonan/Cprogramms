#!/bin/bash

# 参数检查
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <subfolder> <new_project_path>"
  exit 1
fi

SUBFOLDER=$1          # 子文件夹路径（相对主仓库）
NEW_REPO_PATH=$2      # 新项目路径
TEMP_BRANCH=subtree-temp-branch

# 自动跳转到 Git 根目录
cd "$(git rev-parse --show-toplevel)" || { echo "Not inside a git repo"; exit 1; }

echo "📦 Splitting '$SUBFOLDER' into standalone project..."
git subtree split --prefix="$SUBFOLDER" -b $TEMP_BRANCH || { echo "Failed to split subtree"; exit 1; }

echo "📁 Creating new repo at: $NEW_REPO_PATH"
mkdir -p "$NEW_REPO_PATH"
cd "$NEW_REPO_PATH" || exit 1

git init
git pull /d/OneDrive/My\ files/Code/Cprograms $TEMP_BRANCH || { echo "Failed to pull subtree branch from local repo"; exit 1; }
echo "✅ Done. Independent Git repo created at: $NEW_REPO_PATH"

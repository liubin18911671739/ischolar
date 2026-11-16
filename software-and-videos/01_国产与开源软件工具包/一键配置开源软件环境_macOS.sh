#!/usr/bin/env bash
# 一键安装课程开源软件环境（macOS Homebrew 国内镜像加速版）
set -e
echo "=== 正在检查并安装 AI4S 课程开源软件环境 ==="
if command -v brew >/dev/null 2>&1; then
    echo "可按需执行以下命令安装桌面开源软件："
    echo "  brew install --cask obsidian zotero ollama jamovi jasp"
    echo "  brew install node git python uv"
else
    echo "请参考 00_国产与开源软件清单及下载指南.md 从官网直接下载安装包。"
fi

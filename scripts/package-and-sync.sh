#!/usr/bin/env bash
# 一键打包与百度网盘同步脚本
#
# 用法：
#   ./scripts/package-and-sync.sh            # 仅清理 + 重新打包 + 生成 SHA256 清单
#   ./scripts/package-and-sync.sh --sync     # 打包后增量同步至百度网盘并核验远端
#
# 前置条件：
#   - macOS/Linux bash；bypy 同步模式需已安装 uv（使用 `uvx bypy`）并完成百度网盘授权
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLBOX_DIR="$ROOT_DIR/software-and-videos/01_国产与开源软件工具包"
REMOTE_BASE="/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包"
SYNC_MODE=false

[[ "${1:-}" == "--sync" ]] && SYNC_MODE=true

# 判断 Python：优先 3.10+（供 zip 打包脚本使用；本脚本仅用 shell/shutil）
PY="${PY3:-}"
if [[ -z "$PY" ]]; then
  for candidate in "$HOME/miniconda3/bin/python" python3; do
    if "$candidate" -c "import sys; assert sys.version_info >= (3, 10)" >/dev/null 2>&1; then
      PY="$candidate"; break
    fi
  done
fi
[[ -n "$PY" ]] || { echo "❌ 未找到 Python >= 3.10"; exit 1; }

echo "=== 1/4 清理缓存与临时文件 ==="
cd "$ROOT_DIR"
find . -type d \( -name "__pycache__" -o -name ".pytest_cache" -o -name ".venv" -o -name "__MACOSX" \) \
  -not -path "./website/node_modules/*" -not -path "./website/.next/*" -exec rm -rf {} + 2>/dev/null || true
find . -type f \( -name "*.pyc" -o -name ".DS_Store" -o -name "*.bak-*" \) \
  -not -path "./website/node_modules/*" -not -path "./website/.next/*" -delete 2>/dev/null || true

echo "=== 2/4 重新打包 4 个核心压缩包（排除密钥/缓存） ==="
"$PY" - "$TOOLBOX_DIR" <<'PY'
import sys, zipfile, pathlib, datetime

toolbox = pathlib.Path(sys.argv[1])
presets = [
    ("ischolar", "iScholar_v6.2_本地双击即用版_Streamlit_FastAPI.zip"),
    ("lectures/obsidian-vault-template", "Obsidian_科研Vault标准模板与Hermes技能包.zip"),
    ("lectures/核心讲义_Obsidian_Hermes版", "AI4S课程_核心讲义_Obsidian_Hermes版.zip"),
    ("lectures/专题实战讲义_Obsidian_Hermes重构版", "AI4S课程_专题实战讲义_Obsidian_Hermes重构版.zip"),
]
exclude_dirs = {"__pycache__", ".venv", ".pytest_cache", "__MACOSX"}
exclude_names = {"provider_settings.json", ".DS_Store", ".gitignore"}
root = toolbox.parent.parent

for src_rel, out_name in presets:
    src = root / src_rel
    out = toolbox / out_name
    arcroot = src.name
    files = [
        p for p in sorted(src.rglob("*"))
        if p.is_file() and p.name not in exclude_names
        and not any(part in exclude_dirs for part in p.parts)
        and p.suffix not in {".pyc", ".pyo"}
    ]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, str(pathlib.Path(arcroot) / p.relative_to(src)))
    print(f"✔ {out_name}: {len(files)} files, {out.stat().st_size} bytes")
PY

echo "=== 3/4 生成 SHA256 校验清单 ==="
SUMS_FILE="$TOOLBOX_DIR/SHA256SUMS.txt"
{
  echo "# iScholar 随包压缩包校验清单（由 scripts/package-and-sync.sh 生成）"
  echo "# 生成时间：$(date '+%Y-%m-%d %H:%M:%S')"
  echo "# 验证：shasum -a 256 -c SHA256SUMS.txt"
} > "$SUMS_FILE"
for z in "$TOOLBOX_DIR"/iScholar_v6.2_*.zip \
         "$TOOLBOX_DIR"/Obsidian_科研Vault标准模板与Hermes技能包.zip \
         "$TOOLBOX_DIR"/AI4S课程_核心讲义_Obsidian_Hermes版.zip \
         "$TOOLBOX_DIR"/AI4S课程_专题实战讲义_Obsidian_Hermes重构版.zip; do
  shasum -a 256 "$z" | sed "s|$TOOLBOX_DIR/||" >> "$SUMS_FILE"
done
cat "$SUMS_FILE"

if [[ "$SYNC_MODE" != "true" ]]; then
  echo "=== 完成（未同步）。如需同步请运行：./scripts/package-and-sync.sh --sync ==="
  exit 0
fi

echo "=== 4/4 增量同步至百度网盘并核验 ==="
command -v uvx >/dev/null 2>&1 || { echo "❌ 未安装 uv（uvx bypy 不可用）"; exit 1; }

# 同步三个小文件 + 4 个 zip（大视频不在本脚本范围，请单独执行 bypy upload）
declare -a FILES=(
  "00_国产与开源软件清单及下载指南.md"
  "SHA256SUMS.txt"
  "iScholar_v6.2_本地双击即用版_Streamlit_FastAPI.zip"
  "Obsidian_科研Vault标准模板与Hermes技能包.zip"
  "AI4S课程_核心讲义_Obsidian_Hermes版.zip"
  "AI4S课程_专题实战讲义_Obsidian_Hermes重构版.zip"
)
for f in "${FILES[@]}"; do
  src="$TOOLBOX_DIR/$f"
  [[ -f "$src" ]] || { echo "⚠️ 跳过缺失文件：$f"; continue; }
  echo ">>> 上传 $f"
  uvx bypy upload "$src" "$REMOTE_BASE/$f" 2>&1 | tail -n 2 || true
done

echo "--- 远端核验 ---"
uvx bypy list "$REMOTE_BASE" 2>/dev/null || echo "⚠️ 远端列表获取失败，请手动确认"
echo "--- 本地 SHA256 对照 ---"
(
  cd "$TOOLBOX_DIR"
  grep -v '^#' SHA256SUMS.txt | shasum -a 256 -c - || echo "⚠️ 本地校验存在不一致"
)

echo "=== 打包与同步完成 ==="

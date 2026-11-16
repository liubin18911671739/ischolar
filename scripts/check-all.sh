#!/usr/bin/env bash
# 本地一键回归检查：ischolar pytest + website check/build
# 用法：./scripts/check-all.sh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${PY3:-}"
if [[ -z "$PY" ]]; then
  for candidate in "$HOME/miniconda3/bin/python" python3; do
    if "$candidate" -c "import sys; assert sys.version_info >= (3, 10)" >/dev/null 2>&1; then
      PY="$candidate"; break
    fi
  done
fi

echo "=== [1/3] ischolar pytest ==="
cd "$ROOT_DIR/ischolar"
"$PY" -m py_compile app/backend.py app/frontend.py app/prompts.py launcher.py
"$PY" -m pytest tests -q

echo "=== [2/3] website check ==="
cd "$ROOT_DIR/website"
npm run check

echo "=== [3/3] website build ==="
npm run build

echo "=== 全部检查通过 ✅ ==="

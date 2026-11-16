#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=========================================================="
echo "  🎓 正在启动 iScholar 本地科研智能体工作台..."
echo "  - 无需手动配置环境，自动检测依赖并在浏览器中打开"
echo "=========================================================="

# 优先使用已装好 streamlit/fastapi 的本地 Python，否则使用 uv 或自动创建虚拟环境
if [ -x "$HOME/miniconda3/bin/python" ] && "$HOME/miniconda3/bin/python" -c "import streamlit, fastapi, uvicorn, httpx" >/dev/null 2>&1; then
    exec "$HOME/miniconda3/bin/python" "$DIR/launcher.py"
elif command -v python3 >/dev/null 2>&1 && python3 -c "import streamlit, fastapi, uvicorn, httpx" >/dev/null 2>&1; then
    exec python3 "$DIR/launcher.py"
elif command -v uv >/dev/null 2>&1; then
    exec uv run --with fastapi --with "uvicorn[standard]" --with streamlit --with httpx --with pydantic python3 "$DIR/launcher.py"
else
    VENV_DIR="$DIR/.venv"
    if [ ! -d "$VENV_DIR" ]; then
        echo "[iScholar] 首次运行，正在创建独立环境并从国内清华镜像安装依赖..."
        python3 -m venv "$VENV_DIR"
        "$VENV_DIR/bin/pip" install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
        "$VENV_DIR/bin/pip" install -r "$DIR/requirements.txt" -i https://pypi.tuna.tsinghua.edu.cn/simple
    fi
    exec "$VENV_DIR/bin/python" "$DIR/launcher.py"
fi

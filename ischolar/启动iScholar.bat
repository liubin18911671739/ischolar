@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================================
echo   🎓 正在启动 iScholar 本地科研智能体工作台 (Windows)
echo   - 自动检测依赖并在浏览器中打开 http://127.0.0.1:8501
echo ==========================================================

where uv >nul 2>nul
if %errorlevel%==0 (
    uv run --with fastapi --with "uvicorn[standard]" --with streamlit --with httpx --with pydantic python launcher.py
    goto :eof
)

if not exist ".venv\Scripts\python.exe" (
    echo [iScholar] 首次运行，正在创建本地环境并从清华镜像安装依赖...
    python -m venv .venv
    .venv\Scripts\pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
)

.venv\Scripts\python.exe launcher.py
pause

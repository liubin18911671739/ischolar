"""One-click self-bootstrapping launcher for iScholar (Streamlit + FastAPI)."""

from __future__ import annotations

from typing import Optional

import os
import signal
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
BACKEND_PORT = int(os.environ.get("ISCHOLAR_BACKEND_PORT", "8765"))
FRONTEND_PORT = int(os.environ.get("ISCHOLAR_FRONTEND_PORT", "8501"))


def _port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.4)
        return s.connect_ex(("127.0.0.1", port)) == 0


def _ensure_deps() -> None:
    required = ["fastapi", "uvicorn", "streamlit", "httpx", "pydantic"]
    missing = []
    for mod in required:
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    if missing:
        print(f"[iScholar] 正在自动准备首次运行依赖 ({', '.join(missing)})，请稍候...")
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                "-i",
                "https://pypi.tuna.tsinghua.edu.cn/simple",
                *missing,
            ]
        )


def main() -> int:
    os.chdir(ROOT_DIR)
    _ensure_deps()

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT_DIR)
    env["ISCHOLAR_BACKEND_URL"] = f"http://127.0.0.1:{BACKEND_PORT}"

    print("=" * 64)
    print("  🎓 iScholar 本地科研智能体工作台 (Streamlit + FastAPI)")
    print(f"  - FastAPI 后端地址 : http://127.0.0.1:{BACKEND_PORT}/docs")
    print(f"  - Streamlit 前端地址: http://127.0.0.1:{FRONTEND_PORT}")
    print("=" * 64)

    backend_proc: Optional[subprocess.Popen[bytes]] = None
    frontend_proc: Optional[subprocess.Popen[bytes]] = None

    try:
        if not _port_open(BACKEND_PORT):
            backend_proc = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "uvicorn",
                    "app.backend:app",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(BACKEND_PORT),
                ],
                cwd=str(ROOT_DIR),
                env=env,
            )
            for _ in range(40):
                if _port_open(BACKEND_PORT):
                    break
                time.sleep(0.25)

        if not _port_open(FRONTEND_PORT):
            frontend_proc = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "streamlit",
                    "run",
                    "app/frontend.py",
                    "--server.port",
                    str(FRONTEND_PORT),
                    "--server.address",
                    "127.0.0.1",
                    "--server.headless",
                    "true",
                    "--browser.gatherUsageStats",
                    "false",
                ],
                cwd=str(ROOT_DIR),
                env=env,
            )
            for _ in range(40):
                if _port_open(FRONTEND_PORT):
                    break
                time.sleep(0.25)

        url = f"http://127.0.0.1:{FRONTEND_PORT}"
        print(f"[iScholar] 服务已就绪，正在浏览器中打开: {url}")
        if os.environ.get("ISCHOLAR_NO_BROWSER") != "1":
            webbrowser.open(url)

        if frontend_proc is not None:
            frontend_proc.wait()
        elif backend_proc is not None:
            backend_proc.wait()
        return 0
    except KeyboardInterrupt:
        print("\n[iScholar] 正在关闭本地服务...")
        return 0
    finally:
        for proc in (frontend_proc, backend_proc):
            if proc is not None and proc.poll() is None:
                proc.send_signal(signal.SIGTERM)
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()


if __name__ == "__main__":
    raise SystemExit(main())

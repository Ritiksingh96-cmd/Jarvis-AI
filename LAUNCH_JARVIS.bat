@echo off
title JARVIS CORE
color 0b

echo.
echo ========================================================
echo    INITIALIZING JARVIS PERSONAL ASSISTANT
echo ========================================================
echo.

:: 1. Launch UI in "Application Mode" (No browser bars)
echo [SYSTEM] Loading Holographic Interface...
start chrome --app=http://127.0.0.1:5000 --start-maximized || start msedge --app=http://127.0.0.1:5000 || start http://127.0.0.1:5000

:: 2. Start the Backend Core
echo [SYSTEM] Booting Neural Engine...
echo.
echo    [NOTE] Keep this window OPEN in the background!
echo.

:: Use global python directly
python dashboard_server.py

:: If python crashes, pause so user can see error
echo.
echo [ERROR] JARVIS Core crashed!
pause

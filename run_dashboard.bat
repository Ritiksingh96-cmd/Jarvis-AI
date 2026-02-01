@echo off
title JARVIS Dashboard Server
color 0B

echo.
echo ========================================
echo    JARVIS Dashboard Server Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Starting Server...
echo The dashboard should open in your browser automatically.
echo.
echo NOTE: Keep this window OPEN while using the dashboard.
echo.

REM Run Dashboard Server
python dashboard_server.py

echo.
echo ========================================
echo    Server Stopped
echo ========================================
echo.
pause

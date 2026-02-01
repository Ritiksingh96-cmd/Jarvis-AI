@echo off
title JARVIS - AI Assistant
color 0B

echo.
echo ========================================
echo    JARVIS - AI Assistant Launcher
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

echo Starting JARVIS...
echo.

REM Run JARVIS Lite
python jarvis_lite.py

echo.
echo ========================================
echo    JARVIS Shutdown Complete
echo ========================================
echo.
pause

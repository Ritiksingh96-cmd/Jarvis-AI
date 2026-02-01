@echo off
echo ========================================
echo JARVIS Enhanced - Setup Script
echo ========================================
echo.

echo Installing Python dependencies...
echo.

REM Install core dependencies
pip install --upgrade pip
pip install open-interpreter
pip install SpeechRecognition
pip install pyttsx3
pip install pyautogui
pip install rich
pip install python-dotenv

REM Install dashboard dependencies
pip install flask
pip install flask-cors

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run JARVIS, execute:
echo   python jarvis_lite.py
echo.
echo To run the Dashboard:
echo   python dashboard_server.py
echo.
echo Make sure you have your OpenAI API key ready!
echo You can set it as an environment variable:
echo   set OPENAI_API_KEY=your_key_here
echo.
echo Or you'll be prompted to enter it when you run the script.
echo.
pause

@echo off
REM Quick start script for Plaksha RAG Chatbot - Windows

echo.
echo =====================================================
echo    Plaksha University RAG Chatbot - Start Script
echo =====================================================
echo.

REM Check if OpenAI API key is set
if "%OPENAI_API_KEY%"=="" (
    echo ERROR: OPENAI_API_KEY environment variable is not set!
    echo.
    echo Please set your OpenAI API key:
    echo.
    echo In PowerShell:
    echo   $env:OPENAI_API_KEY = "your-api-key-here"
    echo.
    echo In Command Prompt:
    echo   set OPENAI_API_KEY=your-api-key-here
    echo.
    pause
    exit /b 1
)

echo ✓ OpenAI API key detected
echo.

REM Check Python version
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Installing/Updating dependencies...
pip install -q -r requirements.txt

echo.
echo =====================================================
echo   Starting FastAPI Server...
echo =====================================================
echo.
echo Server will run on: http://localhost:8000
echo Once ready, open index.html in your browser
echo.
echo Press Ctrl+C to stop the server
echo.

uvicorn app:app --reload --host 0.0.0.0 --port 8000

pause

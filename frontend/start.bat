@echo off
echo ========================================
echo    Lab-Lens Frontend Startup Script
echo ========================================
echo.

cd /d "%~dp0"

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing dependencies...
    npm install
    if errorlevel 1 (
        echo Failed to install dependencies!
        pause
        exit /b 1
    )
    echo Dependencies installed!
)

echo.
echo ========================================
echo    Starting Lab-Lens Frontend Server
echo ========================================
echo.
echo Frontend running at: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo.

npm run dev

pause

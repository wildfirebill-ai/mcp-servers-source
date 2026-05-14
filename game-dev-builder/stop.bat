@echo off
set "port=25060"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo game-dev-builder on port 25060 stopped.

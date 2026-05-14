@echo off
set "port=25063"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo a11y-advocate on port 25063 stopped.

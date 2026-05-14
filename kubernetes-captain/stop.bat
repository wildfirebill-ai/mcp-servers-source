@echo off
set "port=25022"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo kubernetes-captain on port 25022 stopped.

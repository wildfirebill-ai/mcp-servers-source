@echo off
set "port=25080"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo http-protocol-pro on port 25080 stopped.

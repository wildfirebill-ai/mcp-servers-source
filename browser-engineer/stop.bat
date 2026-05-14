@echo off
set "port=25004"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo browser-engineer on port 25004 stopped.

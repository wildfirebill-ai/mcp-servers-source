@echo off
set "port=25078"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo meta-tag-master on port 25078 stopped.

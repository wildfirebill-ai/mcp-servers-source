@echo off
set "port=25098"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo seed-data-pro on port 25098 stopped.

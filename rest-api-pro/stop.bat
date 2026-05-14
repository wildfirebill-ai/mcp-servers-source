@echo off
set "port=25036"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo rest-api-pro on port 25036 stopped.

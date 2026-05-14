@echo off
set "port=25023"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo ci-cd-engineer on port 25023 stopped.

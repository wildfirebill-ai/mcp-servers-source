@echo off
set "port=25071"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo typography-master on port 25071 stopped.

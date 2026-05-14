@echo off
set "port=25032"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo data-struct-wiz on port 25032 stopped.

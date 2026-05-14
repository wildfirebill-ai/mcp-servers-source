@echo off
set "port=25061"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo mobile-dev-artist on port 25061 stopped.

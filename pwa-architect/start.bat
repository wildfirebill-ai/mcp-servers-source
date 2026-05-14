@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo pwa-architect started on port 25077

@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo a11y-advocate started on port 25063

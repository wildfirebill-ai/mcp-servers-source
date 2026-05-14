@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo cli-commander started on port 25034

@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo cloud-architect started on port 25045

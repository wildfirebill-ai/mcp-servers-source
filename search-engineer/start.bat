@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo search-engineer started on port 25042

@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo mobile-dev-artist started on port 25061

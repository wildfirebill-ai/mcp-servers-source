@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo flask-artist started on port 25015

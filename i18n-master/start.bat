@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo i18n-master started on port 25066

@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo node-crafter started on port 25014

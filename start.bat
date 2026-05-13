@echo off

cd /d "%~dp0"

start http://127.0.0.1:8000/user/dashboard/

python manage.py runserver
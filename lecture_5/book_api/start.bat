@echo off
echo Starting Book API...

call venv\Scripts\activate

uvicorn main:app --reload

pause

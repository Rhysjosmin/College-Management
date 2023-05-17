start "Frontend" cmd /c "venv\Scripts\python.exe -m http.server"
@REM start "Backend" cmd /c "venv\Scripts\activate.bat && python Backend\app.py"
start "Backend" cmd /c "venv\Scripts\activate.bat && flask --app Backend/app run"

start chrome http://127.0.0.1:5000
start chrome http://127.0.0.1:8000/Frontend/

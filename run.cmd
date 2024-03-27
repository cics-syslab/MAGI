@echo off

:: Get the current directory
set "current_dir=%cd%"

:: Check if the current directory is already in PYTHONPATH
echo %PYTHONPATH% | findstr /C:"%current_dir%" >nul
if %errorlevel% neq 0 (
  :: Add the current directory to PYTHONPATH for the current session
  set "PYTHONPATH=%PYTHONPATH%;%current_dir%"
  echo Added %current_dir% to PYTHONPATH for the current session.
) else (
  echo %current_dir% is already in PYTHONPATH for the current session.
)


streamlit run webui\Hello.py

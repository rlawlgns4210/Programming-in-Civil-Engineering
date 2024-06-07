@echo off
REM Set the current directory to the directory of the batch file
cd /d "%~dp0"

REM Save the current directory
set CURRENT_DIR=%cd%

REM Create a virtual environment if it doesn't exist
if not exist "%CURRENT_DIR%\.venv" (
    echo Creating virtual environment...
    python -m venv "%CURRENT_DIR%\.venv"
)

REM Change to the directory containing the virtual environment
cd "%CURRENT_DIR%\.venv\Scripts"

REM Activate the virtual environment
call activate

REM Change to the directory containing the Project directory
cd "%CURRENT_DIR%\Project"

REM Install required Python packages
pip install -r "%CURRENT_DIR%\Project\requirements.txt"

REM Check if the pip install command completed successfully
if %errorlevel% neq 0 (
    echo Failed to install required Python packages. Exiting.
    pause
    exit /b %errorlevel%
)

REM Change to the directory containing the GUI script
cd "%CURRENT_DIR%\Project\GUI"

REM Run the GUI script
python GUI_test.py

REM Check if the GUI script completed successfully
if %errorlevel% neq 0 (
    echo GUI script failed to execute. Exiting.
    pause
    exit /b %errorlevel%
)

REM Pause to allow user to see the output
pause

REM Change to the directory containing the main script
cd "%CURRENT_DIR%\Project\Processor"

REM Run the main script
python main.py

REM Check if the main script completed successfully
if %errorlevel% neq 0 (
    echo Main script failed to execute. Exiting.
    pause
    exit /b %errorlevel%
)

echo Scripts executed successfully.
REM Delete the existing OutputInform.xlsx in Project\Project if it exists
if exist ..\OutputInform.xlsx (
    del ..\OutputInform.xlsx
)

REM Move the OutputInform.xlsx file to the Project directory
move OutputInform.xlsx ..\..\

REM Check if the move command completed successfully
if %errorlevel% neq 0 (
    echo Failed to move OutputInform.xlsx. Exiting.
    pause
    exit /b %errorlevel%
)

REM Pause to allow user to see the output
pause

REM Deactivate the virtual environment
deactivate

@echo off
echo ========================================
echo Exporting Data for Linux Transfer
echo ========================================
echo.

REM Create export directory
set EXPORT_DIR=linux_export
if not exist "%EXPORT_DIR%" mkdir "%EXPORT_DIR%"

REM Copy main data files
echo Copying my_schedule.json...
if exist "my_schedule.json" (
    copy "my_schedule.json" "%EXPORT_DIR%\" >nul
    echo   [OK] my_schedule.json copied
) else (
    echo   [WARNING] my_schedule.json not found
)

echo Copying enhanced_plan_state.json...
if exist "enhanced_plan_state.json" (
    copy "enhanced_plan_state.json" "%EXPORT_DIR%\" >nul
    echo   [OK] enhanced_plan_state.json copied
) else (
    echo   [WARNING] enhanced_plan_state.json not found
)

REM Copy latest backup (optional)
echo Copying latest backup...
for /f "delims=" %%i in ('dir /b /o-d backups\backup_*.json 2^>nul') do (
    copy "backups\%%i" "%EXPORT_DIR%\" >nul
    echo   [OK] Latest backup copied: %%i
    goto :backup_done
)
:backup_done

echo.
echo ========================================
echo Export Complete!
echo ========================================
echo.
echo Your data files are in: %CD%\%EXPORT_DIR%\
echo.
echo Next steps:
echo 1. Transfer the files from %EXPORT_DIR%\ to your Linux machine
echo 2. After git clone on Linux, copy them to the repo directory
echo 3. Run: python3 enhanced_cybersecurity_tracker.py
echo.
echo Files to transfer:
dir /b "%EXPORT_DIR%"
echo.
pause

@echo off
echo Cleaning old build files...
rmdir /s /q build
rmdir /s /q dist
del karaoke_project.spec 2>nul

echo Building the karaoke project into an EXE...
pyinstaller --onefile karaoke_project.py

echo.
echo Build complete! Your EXE is in the 'dist' folder.
pause

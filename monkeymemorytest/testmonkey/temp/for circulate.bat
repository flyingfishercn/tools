@echo off
@set /p inputVersion=version number:

:end
echo  inputversion is%inputVersion% 
FOR /F "tokens=1,* delims=." %%a IN ("%inputVersion%") DO (

echo %%a
set inputVersion=%%b
echo "hello"

goto  end
)

rem CALL SETVERSION %%a %%b %%c  %d %e
pause
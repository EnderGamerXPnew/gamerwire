@echo off
echo pompe.bat
set rep=%cd%
echo %rep%
if %odr% equ out goto:out
cd /d %in%
if exist %scan% cd /d %rep% & copy wire\pools\%buff% %out%
goto:end
:out
cd /d %out%
if exist %scan% cd /d %rep% & copy wire\pools\%buff% %in%
:end
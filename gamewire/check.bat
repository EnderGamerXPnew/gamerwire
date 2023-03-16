@echo off
title gamewire_check

if exist wire goto:true
mkdir wire
cd wire
::stoquage des fichiers structures
mkdir pools
::fichier definissant le chemin des deux jeux auquelle on veut communiquer
(
echo.
)>inout.txt
::fichier idiquant quelle fichier structure doit t'on remplacer, quant un fichier structures est présent dans l'autre jeux
(
echo.
)>equi.txt
cd..
:true
if exist config goto:true
goto:end
:true
rmdir config
echo config
:end
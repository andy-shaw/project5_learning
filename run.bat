@echo off

set use=%1
set silent=%2

if "%silent%"=="s" (set silent="SILENT") else (set silent=" ")

if "%use%"=="n" goto :nondeterministic
if "%use%"=="d" goto :deterministic

goto :error

:deterministic
python learner.py Input_Files\places.txt Input_Files\deterministic_transitions.txt %silent%
goto :end

:nondeterministic
python learner.py Input_Files\places.txt Input_Files\non-deterministic_transitions.txt %silent%
goto :end

:error
echo "USAGE: run.bat n|d [s]"

:end
echo on
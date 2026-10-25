@echo off
cd venv\Scripts\
call activate.bat
python --version
[Console]::OutputEncoding = [System.Text.Encoding]::Unicode

.\venv\Scripts\Activate.ps1
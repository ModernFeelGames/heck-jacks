@echo off
setlocal
cd %APPDATA%
cd ../
cd Local\Programs\Python\Python38-32
cd Scripts

python pywin32_postinstall.py -install.

cd /d %~dp0
pip install -r requirements.txt
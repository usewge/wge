@echo off
color a
echo ## Get last version ##
py updater.py
echo ## Installing Dependencies ##
pip install -r requirements.txt 
echo ## Running Emulator ##
py dist\run.py
pause
 
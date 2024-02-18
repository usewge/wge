@echo off
color a
echo ## Get last version ##
py updater.py
cls
echo ## Installing Dependencies ##
pip install -r requirements.txt
cls
echo ## Running Emulator ##
py dist\run.py 
 
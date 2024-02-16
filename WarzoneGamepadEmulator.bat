@echo off
color a
echo ## Installing Dependencies ##
pip install -r requirements.txt
cls
echo ## Running Emulator ##
py dist\run.py 
 
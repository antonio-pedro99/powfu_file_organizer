@echo off
echo Removing..
reg delete HKEY_CLASSES_ROOT\Directory\Background\shell\powfu
del "C:\Program Files\PowFu - File Organizer"
echo "Removed successfully"
pause
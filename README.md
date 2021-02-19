# covid19
Home to a handy script for getting alerts when COVID vaccine appointments open up in MA.

# Disclaimer
If you aren't comfortable running and maybe even editing Python code, this isn't the tool for you!

# Usage
The `find_vax_ma.py` script has only been tested using Windows 10. Here are some instructions to get you started with Windows 10:

1. Install Python 3.9 from the Microsoft Store
2. Right-click "Start" -> open Windows PowerShell
3. `cd` to the directory where you saved the script
4. `pip install bs4, playsound, requests`
5. `py .\find_vax_ma.py`
6. Ctrl+C when you want to stop the script.

Edit the script to change the URLs (sites) you want to check, the minimum number of available appointments at that site to trigger an alert, what sound to play, and how frequently the script will check.

This script will probably run on OS X but you'll need to specify a different alarm sound, as the default is a Windows 10 system sound.

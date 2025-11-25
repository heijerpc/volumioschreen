the python script is used to control the screen if using volumio.

volumio commands https://developers.volumio.com/api/command-line-client

turning off/on screen (non hdmi)
export DISPLAY=:0
xset q

xset dpms force off       // turn screen off



commands to do 
py --list     shows intalls versions of pyton
py -3.7 -m venv .venv maakt een venv met python 3.7
python -m venv .venv
. .venv/bin/activate     // sourced!!!
pip install RPi.GPIO
versie die we gaan gebruiken is 3


copieer autoScreen.service naar /lib/systemd/system
cmd: sudo cp autoScreen.service /lib/systemd/system

activeren service commandos
cmd: sudo systemctl enable autoScreen
cmd: sudo systemctl start autoScreen

status checken:
cmd: sudo systemctl status autoScreen:
log: journalctl -u autoScreen
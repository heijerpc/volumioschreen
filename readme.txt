the python script is used to control the screen if using volumio.

volumio commands https://developers.volumio.com/api/command-line-client

turning off/on screen (non hdmi)
export DISPLAY=:0
xset q

xset dpms force off       // turn screen off
# Control-Raspberry-Pi-Robot-using-Hand-Gestures
## you can see all details about this project in my youtube channel:
https://www.youtube.com/watch?v=pJess8GuY1A&t=8s
## The parts used in this projects are:
- Raspberry Pi 3 B+
- L298 Motor Driver
- Gearbox DC Motor*4
- Robot chassis
- Some jumper wire

## first you need to install this libraries:
### in Windows:
~~~
pip install opencv-python

pip install mediapipe

pip install paho-mqtt
~~~
### in Raspberry Pi:
~~~
sudo pip install paho-mqtt

sudo apt-get install -y mosquitto mosquitto-clients
~~~
and run this command:
~~~
sudo systemctl enable mosquitto
~~~

# Control-Raspberry-Pi-Robot-using-Hand-Gestures
## you can see all details about this project in my youtube channel:
[video in my Youtube channel](https://www.youtube.com/watch?v=pJess8GuY1A&t=8s).
## Demo
![demo](https://user-images.githubusercontent.com/41531929/147872944-4f840c8c-4e98-4800-9321-3363c96b277f.gif)

## The parts used in this projects are:
- Raspberry Pi 3 B+
- L298 Motor Driver
- Gearbox DC Motor*4
- Robot chassis
- jumper wire

## first you need to install this libraries:
### in Windows:
~~~
pip install opencv-python
~~~
~~~
pip install mediapipe
~~~
~~~
pip install paho-mqtt
~~~
### in Raspberry Pi:
~~~
sudo pip install paho-mqtt
~~~
~~~
sudo apt-get install -y mosquitto mosquitto-clients
~~~
and run this command:
~~~
sudo systemctl enable mosquitto
~~~

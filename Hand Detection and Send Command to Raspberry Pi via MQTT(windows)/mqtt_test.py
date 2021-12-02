import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.0.104"
MQTT_PATH = "test_channel"
import time
while True:
    publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    time.sleep(3)
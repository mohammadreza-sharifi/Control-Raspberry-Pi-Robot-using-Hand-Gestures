import RPi.GPIO as io
import paho.mqtt.client as mqtt

io.setwarnings(False)
io.setmode(io.BOARD)

#define driver pins
#IN1 = 3
#IN2 = 5
#IN3 = 8
#in4 = 10
#setup driver pins
io.setup(3,io.OUT)#IN1
io.setup(5,io.OUT)#IN2
io.setup(8,io.OUT)#IN3
io.setup(10,io.OUT)#IN4

def forward():
    io.output(3,1)
    io.output(5,0)
    io.output(8,1)
    io.output(10,0)
    
#this function moves the robot backward
def backward():
    io.output(3,0)
    io.output(5,1)
    io.output(8,0)
    io.output(10,1)
    
#this function stops the robot
def stopfcn():
    io.output(3,0)
    io.output(5,0)
    io.output(8,0)
    io.output(10,0)
    
#this function moves the robot right
def right():
    io.output(3,1)
    io.output(5,0)
    io.output(8,0)
    io.output(10,0)
    
#this function moves the robot left
def left():
    io.output(3,0)
    io.output(5,0)
    io.output(8,1)
    io.output(10,0)


MQTT_SERVER = "localhost" #specify the broker address, it can be IP of raspberry pi or simply localhost
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, message):
    #print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    if message.payload == b'5':
        forward()
    elif message.payload == b'0':
        stopfcn()
    elif message.payload == b'4':
        backward()
    elif message.payload == b'1':
        left()
    elif message.payload == b'2':
        right()
    else:
        stopfcn()

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_SERVER, 1883, 60) 
    # Connect to the MQTT server and process messages in a background thread. 
    mqtt_client.loop_start() 

if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()

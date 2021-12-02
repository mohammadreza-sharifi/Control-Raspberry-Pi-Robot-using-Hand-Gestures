import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost" #specify the broker address, it can be IP of raspberry pi or simply localhost
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    

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
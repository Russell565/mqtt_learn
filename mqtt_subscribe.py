from paho.mqtt import client as mqtt_client
import time


broker = '192.168.0.102'
port = 1883
topic = '/mqtt/testtopic'
client_id = f'mqtt_czj_subscribe'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to MQTT Broker !')
        else:
            print('Failed to connect, return code %d\n', rc)

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection %s" % rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set("sub")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port, 5)
    return client


def subscribe(client):
    def on_message(client, userdata, msg):
        print(f'Received {msg.payload.decode()} from {msg.topic} topic')
    
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()

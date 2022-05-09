from paho.mqtt import client as mqtt_client
import time


broker = '192.168.0.102'
port = 1883
topic = '/mqtt/testtopic'
client_id = f'mqtt_czj_publish'


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
    client.username_pw_set("pub")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port, 5)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f'msg: {msg_count}'
        result = client.publish(topic, msg)

        status = result[0]
        if status == 0:
            print(f'Send {msg} to topic {topic}')
        else:
            print(f'Failed to send message to topick {topic}')

        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

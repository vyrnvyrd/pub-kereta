# 1301218705 - ALIF RAMDANI
# 1301218681 - FIRNA FIRDIANI
# 1301218683 - MAZID AHMAD

import paho.mqtt.client as mqtt
import json
import ssl
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

host = '9c9c43cc8b12425fbc8c9bca59aca94c.s2.eu.hivemq.cloud'
port = 8883
usrname = 'hivemq.webclient.1672476741794'
passwrd = 'lXZU<;7PW5degA:y3j.8'
context = ssl.create_default_context()

client = mqtt.Client("PKereta1")
client.username_pw_set(usrname, passwrd)
client.on_connect = on_connect
client.tls_set_context(context)
client.tls_insecure_set(True)
client.connect(host, port)
client.loop_start()

E2 = {
    "id": "1",
    "nama_kereta": "Kereta 1",
    "posisi_kereta": "Stasiun A"
}
client.publish("dashboard/kereta", json.dumps(E2))

while True:
    time.sleep(1)
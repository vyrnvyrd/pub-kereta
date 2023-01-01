# 1301218705 - ALIF RAMDANI
# 1301218681 - FIRNA FIRDIANI
# 1301218683 - MAZID AHMAD

import paho.mqtt.client as mqtt
import json

host = '9c9c43cc8b12425fbc8c9bca59aca94c.s2.eu.hivemq.cloud'
port = 8883
usrname = 'hivemq.webclient.1672476741794'
passwrd = 'lXZU<;7PW5degA:y3j.8'

client = mqtt.Client("PKereta1")
client.username_pw_set(usrname, passwrd)
client.connect(host, port)
client.loop_start()

print("publish entitas 2: posisi kereta")
E2 = {
    "id": 1,
    "nama_kereta": "Kereta 2",
    "posisi_kereta": "Stasiun A"
}
client.publish("T2", json.dumps(E2))

client.loop_stop()
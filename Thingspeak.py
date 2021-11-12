# !/usr/bin/python3
from __future__ import print_function
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import requests, os

# Modify URL if this is not running on localhost
host_port = 'http://localhost:8080'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1567770"

# The Write API Key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "EV0WO01IMAM2T2SA"

# The Hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any Username.
mqttUsername = "whatever"

# Your <MQTT-API-KEY> from Account > My Profile.
mqttAPIKey = "6XU6VPLBM2YYHKTH"

# Set your clientID, replace <MY-CLIENTID> with your own text string if you like
clientID = "test1897587"

# Set the transport mode to WebSockets.
tTransport = "websockets"
tPort = 80

topic = "channels/" + channelID + "/publish/" + writeAPIKey
# parameters = {'type': 'devices', 'rid': idx}

# resp = requests.get(host_port + '/json.htm', params=parameters)
# results = resp.json()['result']
# data = results[0]['Data']
#
# data = data.rstrip(' %C')


# build the payload string.
# payload = "field1=" + str(data) + "&field2=" + str(data2)
data = 0

client = mqtt.Client()
client.connect("192.168.137.178", 1883, 60)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/test1")



def Auto(client, userdata, msg):
    global data

    if msg.payload.decode() == "Auto_Gone":
        data -= 1
        payload = "field1=" + str(data)
        try:
            publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
                           auth={'username': mqttUsername, 'password': mqttAPIKey})
            print("no")
        except (KeyboardInterrupt):
            exit(1)

    elif msg.payload.decode() == "Auto_Here":
        data += 1
        payload = "field1=" + str(data)
        try:
            publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
                           auth={'username': mqttUsername, 'password': mqttAPIKey})
            print("si")
        except (KeyboardInterrupt):
            exit(1)
        # client.disconnect()


client.on_connect = on_connect
client.on_message = Auto
client.loop_forever()

# attempt to publish this data to the topic.
# try:
#     publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
#                    auth={'username': mqttUsername, 'password': mqttAPIKey})
# except (KeyboardInterrupt):
#     exit(1)


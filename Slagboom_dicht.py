#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json

MQTT_host = "192.168.137.178"
MQTT_port = 1883

MQTT_channel = "domoticz/in"
MQTT_message = json.dumps({"command": "switchlight", "idx": 3, "switchcmd": "Off" })


# This is the Publisher
client = mqtt.Client()
client.connect(MQTT_host,MQTT_port,60)
client.publish(MQTT_channel, MQTT_message)
client.disconnect()


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIN = 23
GPIO.setup(PIN, GPIO.IN)

print ("Start sensor...")
time.sleep(2)
print ("Sensor werkend...")

while True:
   if GPIO.input(PIN):
      print ("Beweging gedetecteerd! " + (time.strftime("%H:%M:%S")))
      time.sleep(2)
      ####################
      import paho.mqtt.client as mqtt
      import json

      MQTT_host = "192.168.137.178"
      MQTT_port = 1883

      MQTT_channel = "domoticz/in"
      MQTT_message = json.dumps({"command": "switchlight", "idx": 3, "switchcmd": "On" })

      x = 0

      while x <= 10:
      # This is the Publisher
        client = mqtt.Client()
        client.connect(MQTT_host,MQTT_port,60)
        client.publish(MQTT_channel, MQTT_message)
        client.disconnect()

        x += 1
      
      #####################
      time.sleep(10)
      import paho.mqtt.client as mqtt
      import json

      MQTT_host = "192.168.137.178"
      MQTT_port = 1883

      MQTT_channel = "domoticz/in"
      MQTT_message = json.dumps({"command": "switchlight", "idx": 3, "switchcmd": "Off" })
      MQTT_channel2 = "test/test1"
      MQTT_message2 = "Auto_Gone"

        # This is the Publisher
      client = mqtt.Client()
      client.connect(MQTT_host,MQTT_port,60)
      client.publish(MQTT_channel, MQTT_message)
      client.publish(MQTT_channel2, MQTT_message2)
      client.disconnect()
      #########################
      time.sleep(10)
      
      
   else:
       print('Niet gedecteerd!!!')
   time.sleep(2)

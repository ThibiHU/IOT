import time
import RPi.GPIO as GPIO
import mfrc522
from termcolor import colored
import json
import paho.mqtt.client as mqtt
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

# Welcome message
wachten=("Aan het wachten voor een pas...\n")
print(wachten)
def pulse(pin_nr, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """

    pin_nr = 18
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)


led = 18
GPIO.setup(led, GPIO.OUT)

# Create an object of the class MFRC522
MIFAREReader = mfrc522.MFRC522()


# This loop checks for chips. If one is near it will get the UID
try:

    while True:
        x=0
        f= open("UID.txt", "r")
        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
            gescande_uid= (str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))
            for UID in f.readlines():
                if UID.strip()==gescande_uid.strip():
                    print()
                    print(colored('Welkom! Slagboom gaat open!!!', 'green'))
                    pulse(led, 0.2, 0.2)
                    time.sleep(2)
                    print(wachten+'\n\n')
                    x=1
                    MQTT_host = "192.168.137.178"
                    MQTT_port = 1883

                    MQTT_channel = "domoticz/in"
                    MQTT_message = json.dumps({"command": "switchlight", "idx": 3, "switchcmd": "On" })

                    z = 0

                    while z <= 10:
                    # This is the Publisher
                        client = mqtt.Client()
                        client.connect(MQTT_host,MQTT_port,60)
                        client.publish(MQTT_channel, MQTT_message)
                        client.disconnect()

                        z += 1
                    #####################################3
                    # Needed modules will be imported and configured
                    import RPi.GPIO as GPIO
                    import time

                    GPIO.setmode(GPIO.BCM)

                    # Declaration of the input pin which is connected with the sensor
                    GPIO_PIN = 21
                    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

                    # Break between the results will be defined here (in seconds)
                    delayTime = 2.0

                    # main loop
                    try:
                            while True:
                                if GPIO.input(GPIO_PIN) == False:
                                    print ("Wel auto")
                                    time.sleep(5)
                                    if GPIO.input(GPIO_PIN) == True:
                                        import paho.mqtt.client as mqtt
                                        import json

                                        MQTT_host = "192.168.137.178"
                                        MQTT_port = 1883

                                        MQTT_channel = "domoticz/in"
                                        MQTT_message = json.dumps({"command": "switchlight", "idx": 3, "switchcmd": "Off" })
                                        MQTT_channel2 = "test/test1"
                                        MQTT_message2 = "Auto_Here"
                                       
                                       

                                        # This is the Publisher
                                        client = mqtt.Client()
                                        client.connect(MQTT_host,MQTT_port,60)
                                        client.publish(MQTT_channel, MQTT_message);
                                        client.publish(MQTT_channel2, MQTT_message2);
                                        client.disconnect()
                                        break
                                       
                     
                                else:
                                    print ("Geen auto")

                                # Reset + Delay
                                time.sleep(delayTime)

                    # Scavenging work after the end of the program
                    except KeyboardInterrupt:
                            GPIO.cleanup()

                    #####################################    
                    break
                   
                   
                   
            if x!=1:
                    print(colored('Pas foutief of niet herkend. Probeer opnieuw!', 'red'))
                    pulse(led, 0.2, 0.2)
                    pulse(led, 0.2, 0.2)
                    pulse(led, 0.2, 0.2)
                    time.sleep(2)
                    print(wachten+'\n\n')
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

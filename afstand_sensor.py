import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

sr04_trig = 20
sr04_echo = 21

GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

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


   

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """

   # send trigger pulse
   # inplement this step
   while True:
      GPIO.output(trig_pin, False)
      print("Ëven wachten....")
      #time.sleep(0.2)

      GPIO.output(trig_pin, True)
      time.sleep(0.2)
      GPIO.output(trig_pin, False)

   # wait for echo high and remember its start time
   # inplement this step
      while GPIO.input(echo_pin)==0:
         start_pulse = time.time()

   # wait for echo low and remember its end time
   # inplement this step
      while GPIO.input(echo_pin) == 1:
         end_pulse = time.time()

   # calculate and return distance
   # inplement this step
      looptijd = end_pulse - start_pulse
      afstand = looptijd * 17150
      print("Afstand is: ", afstand, "cm")
     
      if afstand <= 40:
          pulse(led, 0.2, 0.2)
while True:
   print( sr04( sr04_trig, sr04_echo ))
   time.sleep( 0.5 )

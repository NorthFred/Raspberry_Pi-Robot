# Version: SS v.0.0.3 | Last modified: 2016.12.30
# Written for SW-420 Shock / Vibration Sensor Module


import RPi.GPIO as GPIO
from time import sleep


#vibr_pin = 16
#shock_threshold = 100   # Higher value = higher threshold.  Manual sensitivity is set to max.

class Shock_Probing():
    

    def __init__(self, vibr_pin, shock_threshold):

        self.__vibr_pin = vibr_pin
        self.__shock_threshold = shock_threshold

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__vibr_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        GPIO.add_event_detect(self.__vibr_pin, GPIO.BOTH, callback = self.callback, bouncetime = 1)

        self.count = 0


    def callback(self, __vibr_pin):

        self.count +=1


    def register_shocks(self):

        while True:

            sleep(1)

            if self.count >= self.__shock_threshold:

                print "Shock Threshold exceeded"

            else:

                pass




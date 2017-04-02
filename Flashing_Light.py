# Version: FL v.0.0.5 | Last modified: 2016.12.20
# Written for KEYES KY-016

import RPi.GPIO as GPIO
from time import sleep


class LED_Control():

        def __init__(self, R_pin, G_pin, B_pin, R_freq, G_freq, B_freq, R_dcycle, G_dcycle, B_dcycle):

                self.__R_pin = R_pin
                self.__G_pin = G_pin
                self.__B_pin = B_pin
                self.__R_freq = R_freq
                self.__G_freq = G_freq
                self.__B_freq = B_freq
                self.__R_dcycle = R_dcycle
                self.__G_dcycle = G_dcycle
                self.__B_dcycle = B_dcycle
                
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.__R_pin, GPIO.OUT)
                GPIO.setup(self.__G_pin, GPIO.OUT)
                GPIO.setup(self.__B_pin, GPIO.OUT)
                

        def flashing_light(self):

                self.r = GPIO.PWM(self.__R_pin, self.__R_freq)
                self.g = GPIO.PWM(self.__G_pin, self.__G_freq)
                self.b = GPIO.PWM(self.__B_pin, self.__B_freq)

                self.r.start(self.__R_dcycle)
                self.g.start(self.__G_dcycle)
                self.b.start(self.__B_dcycle)


        def stop_flashing(self):

                self.r.stop()
                self.g.stop()
                self.b.stop()
                

        def constant_RED_light_on(self):

                GPIO.output(self.__R_pin, GPIO.HIGH)
                GPIO.output(self.__G_pin, GPIO.LOW)
                GPIO.output(self.__B_pin, GPIO.LOW)


        def constant_GREEN_light_on(self):

                GPIO.output(self.__R_pin, GPIO.LOW)
                GPIO.output(self.__G_pin, GPIO.HIGH)
                GPIO.output(self.__B_pin, GPIO.LOW)
                

        def constant_BLUE_light_on(self):

                GPIO.output(self.__R_pin, GPIO.LOW)
                GPIO.output(self.__G_pin, GPIO.LOW)
                GPIO.output(self.__B_pin, GPIO.HIGH)
                

        def constant_YELLOW_light_on(self):

                GPIO.output(self.__R_pin, GPIO.HIGH)
                GPIO.output(self.__G_pin, GPIO.HIGH)
                GPIO.output(self.__B_pin, GPIO.LOW)
                

        def constant_WHITE_light_on(self):

                GPIO.output(self.__R_pin, GPIO.HIGH)
                GPIO.output(self.__G_pin, GPIO.HIGH)
                GPIO.output(self.__B_pin, GPIO.HIGH)


        def constant_CYAN_light_on(self):

                GPIO.output(self.__R_pin, GPIO.LOW)
                GPIO.output(self.__G_pin, GPIO.HIGH)
                GPIO.output(self.__B_pin, GPIO.HIGH)
                

        def constant_MAGI_light_on(self):

                GPIO.output(self.__R_pin, GPIO.HIGH)
                GPIO.output(self.__G_pin, GPIO.LOW)
                GPIO.output(self.__B_pin, GPIO.HIGH)


        def constant_light_off(self):
                
                GPIO.output(self.__R_pin, GPIO.LOW)
                GPIO.output(self.__G_pin, GPIO.LOW)
                GPIO.output(self.__B_pin, GPIO.LOW)


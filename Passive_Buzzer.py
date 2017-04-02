# Version: PB v.0.0.3 | Last Modified: 2017.02.02
# Written for Passive Buzzer Modules with low trigger signal

import RPi.GPIO as GPIO
from time import sleep

class Buzzer_Sound():

	def __init__(self, buzzer_pin):
	
		self.buzzer_pin = buzzer_pin
		
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.buzzer_pin, GPIO.OUT)
	
	
	def beep(self, freq, duration):		# Feeding waves, since no oscillator present in passive buzzer module
	
		if freq == 0:					# Higher frequency == higher pitch
			
			sleep(duration)
			
			return

		period = 1.0 / freq					# Period = (sec/cycle) is inverse of frequency (cyc/sec)
		delay = period / 2					# Half of the wave
		cycles = int(duration * freq)		# Amount of waves = duration * frequency
		
		for i in range (cycles):
		
			GPIO.output(self.buzzer_pin, False)
			sleep(delay)
			GPIO.output(self.buzzer_pin, True)
			sleep(delay)

			
	# Police siren sound
	
	def pwm_siren(self):
		
		try:
		
			pwm = GPIO.PWM(self.buzzer_pin, 900)
		
			i = 0
			
			pwm.start(0)
		
			for i in range (0, 4):
			
				pwm.ChangeFrequency(900)
							
				for dc in range (0, 101, 10):
				
					pwm.ChangeDutyCycle(dc)
					sleep(0.05)
					
				pwm.ChangeFrequency(450)
				
				for dc in range (100, -1, -10):
				
					pwm.ChangeDutyCycle(dc)
					sleep(0.05)

		except KeyboardInterrupt:
			
			pass

		pwm.stop(0)
		#GPIO.cleanup()                    # Commented out, main program uses this.

		
	# Low, medium and high beeps		
			
	def beep_low(self):
	
		self.beep(120, 0.1)
	
	def beep_medium(self):
	
		self.beep(600, 0.2)
		
	def beep_high(self):
	
		self.beep(1000, 0.2)

		
	# Error beep
	
	def beep_error_1(self):
	
		self.si1()

	def beep_error_2(self):
	
		self.fa1()
		self.sol1()
		self.si1()
		
	def beep_input_movement(self):
	
		self.mi1()
	
	def beep_input_motor_stop(self):
	
		self.fa1()
		
	# Combo beep

	def combo_beep(self):
	
		self.beep_high()
		sleep(0.2)
		self.beep_medium()
		sleep(0.2)
		self.beep_low()
		sleep(0.2)
		self.beep_low()
		sleep(0.2)	
		self.beep_low()
		sleep(0.2)
		

	# Music notes	
		
	def do1(self):

		self.beep(262, 0.1)
		
	def re1(self):
	
		self.beep(294, 0.1)
	
	def mi1(self):
	
		self.beep(330, 0.1)
		
	def fa1(self):
	
		self.beep(349, 0.1)
		
	def sol1(self):
	
		self.beep(392, 0.1)
		
	def la1(self):
	
		self.beep(440, 0.1)
		
	def si1(self):
	
		self.beep(494, 0.1)
		
	def do2(self):
	
		self.beep(523, 0.1)
		
	def re2(self):
	
		self.beep(587, 0.1)
		
	def mi2(self):
	
		self.beep(659, 0.1)

	def fa2(self):
	
		self.beep(698, 0.1)
	
	def sol2(self):
	
		self.beep(784, 0.1)
		
	def la2(self):
	
		self.beep(880, 0.1)
		
	def si2(self):
	
		self.beep(998, 0.1)

	
	# Mario tune, underworld tune

	def familiar_tune(self):

		notes = {
			'B0' : 31,
			'C1' : 33, 'CS1' : 35,
			'D1' : 37, 'DS1' : 39,
			'E1' : 41,
			'F1' : 44, 'FS1' : 46,
			'G1' : 49, 'GS1' : 52,
			'A1' : 55, 'AS1' : 58,
			'B1' : 62,
			'C2' : 65, 'CS2' : 69,
			'D2' : 73, 'DS2' : 78,
			'E2' : 82,
			'F2' : 87, 'FS2' : 93,
			'G2' : 98, 'GS2' : 104,
			'A2' : 110, 'AS2' : 117,
			'B2' : 123,
			'C3' : 131, 'CS3' : 139,
			'D3' : 147, 'DS3' : 156,
			'E3' : 165,
			'F3' : 175, 'FS3' : 185,
			'G3' : 196, 'GS3' : 208,
			'A3' : 220, 'AS3' : 233,
			'B3' : 247,
			'C4' : 262, 'CS4' : 277,
			'D4' : 294, 'DS4' : 311,
			'E4' : 330,
			'F4' : 349, 'FS4' : 370,
			'G4' : 392, 'GS4' : 415,
			'A4' : 440, 'AS4' : 466,
			'B4' : 494,
			'C5' : 523, 'CS5' : 554,
			'D5' : 587, 'DS5' : 622,
			'E5' : 659,
			'F5' : 698, 'FS5' : 740,
			'G5' : 784, 'GS5' : 831,
			'A5' : 880, 'AS5' : 932,
			'B5' : 988,
			'C6' : 1047, 'CS6' : 1109,
			'D6' : 1175, 'DS6' : 1245,
			'E6' : 1319,
			'F6' : 1397, 'FS6' : 1480,
			'G6' : 1568, 'GS6' : 1661,
			'A6' : 1760, 'AS6' : 1865,
			'B6' : 1976,
			'C7' : 2093, 'CS7' : 2217,
			'D7' : 2349, 'DS7' : 2489,
			'E7' : 2637,
			'F7' : 2794, 'FS7' : 2960,
			'G7' : 3136, 'GS7' : 3322,
			'A7' : 3520, 'AS7' : 3729,
			'B7' : 3951,
			'C8' : 4186, 'CS8' : 4435,
			'D8' : 4699, 'DS8' : 4978
		}

		underworld_melody = [
			  notes['C4'], notes['C5'], notes['A3'], notes['A4'],
			  notes['AS3'], notes['AS4'], 0,
			  0,
			  notes['C4'], notes['C5'], notes['A3'], notes['A4'],
			  notes['AS3'], notes['AS4'], 0,
			  0
			]

		underworld_tempo = [
			  12, 12, 12, 12,
			  12, 12, 6,
			  3,
			  12, 12, 12, 12,
			  12, 12, 6,
			  3
			]
			
		def play(melody,tempo,pace=0.800):
    
			for i in range(0, len(melody)):        # Play song
				
				noteDuration = pace/tempo[i]
				self.beep(melody[i],noteDuration)    # Change the frequency along the song note
				
				pauseBetweenNotes = noteDuration * 1.30
				sleep(pauseBetweenNotes)

		play(underworld_melody, underworld_tempo, 0.800)	


##########################################
# --- BELOW CODE IS FOR TESTING ONLY --- #
##########################################

#buzzer_pin = 18

#PB = Buzzer_Sound(buzzer_pin)

#PB.beep_low()
#sleep(0.5)
#PB.beep_medium()
#sleep(0.5)
#PB.beep_high()

#PB.do1()
#sleep(0.15)
#PB.do1()
#sleep(0.15)
#PB.do2()
#sleep(0.15)
#PB.do2()
#sleep(0.15)
#PB.do1()
#sleep(0.15)
#PB.do1()

#PB.beep_input_movement()

#GPIO.cleanup()



#PB.pwm_siren()

#PB.familiar_tune()

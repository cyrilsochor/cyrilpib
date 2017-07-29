#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
from datetime import datetime
import time

INPUT_PIN = 18
MONITOR_DELAY = 0.01 # in seconds
MONITOR_INERATIONS = 200 # *DELAY = 2 seconds

GPIO.setmode(GPIO.BCM)

GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def log(msg):
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + " " + msg, flush=True)

log("STARTED")

while True:
	GPIO.wait_for_edge(INPUT_PIN, GPIO.FALLING)
	log("SHUTDOWN?")
	for i in range(MONITOR_INERATIONS):
		if GPIO.input(INPUT_PIN) != GPIO.LOW:
			#log("SHUTDOWN-NO")
			break
		time.sleep (MONITOR_DELAY);
	else:
		log("SHUTDOWN")
		subprocess.call(['shutdown', "-h", "now"], shell=False)
		#subprocess.Popen(['shutdown', "-h", "now"], shell=False)
			
	


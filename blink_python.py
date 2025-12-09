import time
import RPi.GPIO as GPIO

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.2)

finally:
    GPIO.output(PIN, GPIO.LOW)
    GPIO.cleanup()

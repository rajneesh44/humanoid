import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(12.5)


q = GPIO.PWM(35, 50)
q.start(12.5)
try:
    while True:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        q.ChangeDutyCycle(7.5)
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        q.ChangeDutyCycle(2.5)
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        q.ChangeDutyCycle(12.5)
        time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
    p.stop()
    q.stop()
    GPIO.cleanup()

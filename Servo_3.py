import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(35, gpio.OUT)
p = gpio.PWM(12, 50)
p.start(12.5)

q = gpio.PWM(35,50)
q.start(12.5)

gpio.setup(11,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.OUT)
gpio.output(11,True)
gpio.output(15,True)
gpio.output(16,True)
gpio.output(18,True)
    
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
        
        gpio.output(11,True)
        gpio.output(15,False)
        gpio.output(16,True)
        gpio.output(18,False)
        time.sleep(2)
        print("motor is running forward")
        gpio.output(11,False)
        gpio.output(15,True)
        gpio.output(16,False)
        gpio.output(18,True)
        time.sleep(2)
        print("motors running back")
except KeyboardInterrupt:
    p.stop()
    q.stop()
    gpio.cleanup()

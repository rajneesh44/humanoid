import RPi.GPIO as io
import time

io.cleanup()
io.setmode(io.BCM)

ma1 = 17
ma2 = 27
mb1 = 22
mb2 = 23
ena = 24
enb = 25
s1 = 18
s2 = 19
s3 = 13
s4 = 12
    
io.setup(s1,io.OUT)
io.setup(s2,io.OUT)
io.setup(s3,io.OUT)
io.setup(s4,io.OUT)
p =io.PWM(s1,50)
p.start(7.5)
q =io.PWM(s2,50)
q.start(7.5)
r =io.PWM(s3,50)
r.start(7.5)
s =io.PWM(s4,50)
s.start(7.5)


#def init():
#    io.setup(ma1,io.OUT)
#    io.setup(ma2,io.OUT)
#    io.setup(mb1,io.OUT)
#    io.setup(mb2,io.OUT)
#    io.setup(ena,io.OUT)
#    io.setup(enb,io.OUT)
#    
#def stop():
#    io.output(ma1,False)
#    io.output(ma2,False)
#    io.output(mb1,False)
#    io.output(mb2,False)
#    
#def forward(x):
#    init()
#    io.output(ena,True)
#    io.output(enb,True)
#    io.output(ma1,True)
#    io.output(ma2,False)
#    io.output(mb1,True)
#    io.output(mb2,False)
#    time.sleep(x)
#    io.output(ma1,False)
#    io.output(ma2,True)
#    io.output(mb1,False)
#    io.output(mb2,True)
#    time.sleep(1)
    
#def backward(x):
#    init()
#    io.output(ena,True)
#    io.output(enb,True)
#    io.output(ma1,False)
#    io.output(ma2,True)
#    io.output(mb1,False)
#    io.output(mb2,True)
#    time.sleep(x)
#    io.output(ma1,True)
#    io.output(ma2,False)
#    io.output(mb1,True)
#    io.output(mb2,False)
#    time.sleep(1)
    

def servo(x):
    p.ChangeDutyCycle(12.5)
    q.ChangeDutyCycle(12.5)
    time.sleep(x)
    r.ChangeDutyCycle(12.5)
    s.ChangeDutyCycle(12.5)
    time.sleep(x)
    r.ChangeDutyCycle(7.5)
    s.ChangeDutyCycle(7.5)
    time.sleep(x)
    p.ChangeDutyCycle(7.5)
    q.ChangeDutyCycle(7.5)
    time.sleep(x)
    
try:
    while(1):
        #forward(4)
        servo(2)
        time.sleep(1)
        #backward(4)
        servo(2)
        time.sleep(1)
        
except KeyboardInterrupt:
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    io.cleanup()
    
finally:
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    io.cleanup()
        
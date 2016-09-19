import RPi.GPIO as GPIO
import time
from sakshat import SAKSHAT
SAKS = SAKSHAT()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)#connect to A4988 STEP
GPIO.setup(24,GPIO.OUT)#connect to A4988 DIR
GPIO.setup(27,GPIO.OUT)#connect to A4988 ENABLE

GPIO.output(27,GPIO.LOW)
GPIO.output(24,GPIO.HIGH)
def s_do(t):
    #Sound_Do

while 1:
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.001)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.001)

for i in range(1,2000):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00052)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00052)
time.sleep(.3)
for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00124)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00124)
time.sleep(.3)
for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0011)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0011)
time.sleep(.3)
for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00098)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00098)
time.sleep(.3)

for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0009)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0009)
time.sleep(.3)
GPIO.output(24,GPIO.LOW)
for i in range(1,100):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0008)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0008)
time.sleep(.3)

GPIO.output(24,GPIO.HIGH)
for i in range(1,120):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0007)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0007)
time.sleep(.3)
GPIO.output(24,GPIO.LOW)
for i in range(1,150):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00065)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00065)
time.sleep(.3)
for i in range(1,150):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00058)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00058)
time.sleep(.3)
for i in range(1,150):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00058)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00058)
time.sleep(.3)
for i in range(1,150):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00058)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00058)
time.sleep(1)
for i in range(1,150):
    #G
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00058)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00058)
time.sleep(.3)
GPIO.output(24,GPIO.LOW)
for i in range(1,150):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.00065)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.00065)
time.sleep(.3)

GPIO.output(24,GPIO.HIGH)
for i in range(1,120):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0007)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0007)
time.sleep(.3)
GPIO.output(24,GPIO.LOW)
for i in range(1,100):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0008)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0008)
time.sleep(.3)

for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0009)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0009)
time.sleep(.3)

for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0009)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0009)
time.sleep(.3)
for i in range(1,80):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.0009)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.0009)
time.sleep(.3)



    
print('over')


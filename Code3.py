# Code 3 : StepperMotor_3 – Continuous Bidirectional Rotation

from machine import Pin
import time

# Objective : Write a program where the motor performs one full rotation in one direction followed by one full rotation in the opposite direction, continuously.

l1 = Pin(14, Pin.OUT)
l2 = Pin(25, Pin.OUT)
l3 = Pin(26, Pin.OUT)
l4 = Pin(27, Pin.OUT)

power = [[1,1,0,0], [0,1,0,0], [0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1], [1,0,0,1],[1,0,0,0]]
coil = [l1, l2, l3, l4]

# Expected Functional Behavior :

while True:
    
# One complete clockwise rotation.

    for a in range(250):
        for step in power:
            l4.value(step[0])
            l3.value(step[1])
            l2.value(step[2])
            l1.value(step[3])
            time.sleep(0.005)
            
# One complete counterclockwise rotation.

    for a in range(250):
        for step in reversed(power):
            l4.value(step[0])
            l3.value(step[1])
            l2.value(step[2])
            l1.value(step[3])
            time.sleep(0.005)
            
# This sequence should repeat continuously.



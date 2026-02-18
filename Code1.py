# Code 1 : StepperMotor_1 – Continuous Rotation (Single Direction)

from machine import Pin
import time

# Objective : Write a program to rotate the stepper motor continuously in one direction.

l1 = Pin(14, Pin.OUT)
l2 = Pin(25, Pin.OUT)
l3 = Pin(26, Pin.OUT)
l4 = Pin(27, Pin.OUT)

power = [[1,1,0,0], [0,1,0,0], [0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1], [1,0,0,1],[1,0,0,0]]
coil = [l1, l2, l3, l4]

# Expected Functional Behavior :
# The motor should rotate continuously (clockwise or counterclockwise).
# The stepping sequence must be implemented using a list.

while True :
    
    for step in power:
        for i in range(len(coil)):
            coil[i].value(step[i])
            coil[i].value(step[i])
            coil[i].value(step[i])
            coil[i].value(step[i])
            time.sleep(0.001)




        







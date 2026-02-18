# Code 2 : StepperMotor_2 – Two Complete Rotations

from machine import Pin
import time

# Objective : Write a program to rotate the stepper motor exactly two full revolutions and then stop.

l1 = Pin(14, Pin.OUT)
l2 = Pin(25, Pin.OUT)
l3 = Pin(26, Pin.OUT)
l4 = Pin(27, Pin.OUT)

power = [[1,1,0,0], [0,1,0,0], [0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1], [1,0,0,1],[1,0,0,0]]
coil = [l1, l2, l3, l4]

# Expected Functional Behavior : 
# The motor should complete two full rotations.
# After completing the rotations, the motor must stop.
rotation = 2000 * 2
steps = 0
while steps <= rotation :
      
        for step in power:
            if steps <= rotation :
                for i in range(len(coil)):
                    coil[i].value(step[i])
                    coil[i].value(step[i])
                    coil[i].value(step[i])
                    coil[i].value(step[i])
                    
                steps += 1
                time.sleep(0.005) 

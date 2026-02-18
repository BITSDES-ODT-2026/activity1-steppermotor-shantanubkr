# Code 4 : StepperMotor_TwoPushButton – Continuous Direction Control Using Two Push Buttons

from machine import Pin
import time

# Objective : Write a program to control motor direction using two push buttons.

l1 = Pin(14, Pin.OUT)
l2 = Pin(25, Pin.OUT)
l3 = Pin(26, Pin.OUT)
l4 = Pin(27, Pin.OUT)
pb1 = Pin(18, Pin.IN, Pin.PULL_UP)
pb2 = Pin(19, Pin.IN, Pin.PULL_UP)

power = [[1,1,0,0], [0,1,0,0], [0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1], [1,0,0,1],[1,0,0,0]]
coil = [l1, l2, l3, l4]

# Expected Functional Behavior :

while True:
    
# Button 1 → Motor rotates continuously clockwise.

    pb1_v = pb1.value()
    pb2_v = pb2.value()

    if pb1_v == 0 and pb2_v == 1 :
            for step in power:
                l4.value(step[0])
                l3.value(step[1])
                l2.value(step[2])
                l1.value(step[3])
                time.sleep(0.005)
            
# Button 2 → Motor rotates continuously counterclockwise.
    elif pb1_v == 1 and pb2_v == 0 :
            for step in reversed(power):
                l4.value(step[0])
                l3.value(step[1])
                l2.value(step[2])
                l1.value(step[3])
                time.sleep(0.005)
            
# The motor should respond in real time to button input.

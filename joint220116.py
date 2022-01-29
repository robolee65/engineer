#Robotis MicroPython
from pycm import *

m1=DXL(1)
m2=DXL(2)
m3=DXL(3)
m4=DXL(4)
dxlbus.torque_on()

m1.write32(112,100)
m2.write32(112,100)
m3.write32(112,100)
m4.write32(112,100)

m4.goal_position(1024)
delay(1000)
    
m4.goal_position(3072)
delay(1000)

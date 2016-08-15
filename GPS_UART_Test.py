import serial
from time import sleep

port = '/dev/ttyAMA0'
gnss = serial.Serial(port,baudrate=9600, timeout=1.0)
gnss.flushInput()
while True:
    if (gnss.inWaiting()>0):
        input = gnss.readline()
        print(input)

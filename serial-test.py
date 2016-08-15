import serial
port = '/dev/ttyAMA0'
gnss = serial.Serial(port,baudrate=9600, timeout=3.0)

while True:
    gnss.write("\r\nSay Something:")
    rcv = gnss.read(10)
    gnss.write("\r\nYou sent:"+repr(rcv))

#!/usr/bin/python
from SimpleCV import Image, Display
from time import sleep

display = Display()
raspberriImage = Image("raspberries.jpg")

raspberriImage.save(display)

while display.isNotDone():
    sleep(0.1)
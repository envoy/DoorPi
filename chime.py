#!/usr/bin/python
# 2014 Wells Riley

import time
import RPi.GPIO as GPIO
import pygame
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the Door Sensor on GPIO pin 23
door_pin = 23
GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up Red LED on GPIO pin 4
red_led = 4
GPIO.setup(red_led, GPIO.OUT)
GPIO.output(red_led,False)

# Set up Green LED on GPIO pin 19
green_led = 17
GPIO.setup(green_led, GPIO.OUT)
GPIO.output(green_led,False)

# Set up the music player
audio_file = '/home/pi/tng_chime_clean.wav'
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.set_volume(1)

# Listen for the door to open
opened = 0
GPIO.output(red_led,True)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
print("listening...")

try:
    while True:
        if GPIO.input(door_pin):
            if opened == 0:
                print("door opened")
                GPIO.output(red_led,False)
                GPIO.output(green_led,True)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                opened = 1

        else:
            if opened == 1:
                print("door closed")
                GPIO.output(green_led,False)
                GPIO.output(red_led,True)
                opened = 0

except KeyboardInterrupt:
    GPIO.cleanup()
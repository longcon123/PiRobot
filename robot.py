#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import threading
import speech_recognition as sr
import os
import pyaudio
import serial
from gtts import gTTS
from threading import Thread
data =21                

def command():
	global data
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listen...")
		r.pause_threshold = 1
		r.threshold_energy = 2000
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try:
		comand = r.recognize_google(audio, language='vi-VN')
		print("Ban noi:" + comand)
		if u"iến" in comand:
			data = 1
		elif u"cơm" in comand:
			data = 2
		elif u"rái" in comand:
			data = 4
		elif u"hải" in comand:
			data = 3
		elif u"ừng" in comand:
			data = 0
		elif u"iường" in comand:
			data = 5
##	elif u"thịt" in comand:
##		data = 6
##	elif u"cơm" in comand:
##		data = 7
	except	sr.UnknownValueError:
		print(sr.UnknownValueError)
##def talk(cm):
##        tts = gTTS(text=cm, lang='vi')
##        tts.save('audio.wav')
##        os.system('omxplayer audio.wav')
def runA():
	
	while True:
		command()
def runB():
	try:
		ard = serial.Serial('/dev/ttyACM0', 115200)
		ard1 = serial.Serial('/dev/ttyUSB0', 9600)
	except:
		ard = serial.Serial('/dev/ttyACM0', 115200)
		ard1 = serial.Serial('/dev/ttyUSB1', 9600)
	global data
	while True:
		if data == 1:
			ard.write(('1'.encode()))
			time.sleep(1)
			ard.write(('0'.encode()))
			data = 6
		if data == 2:
			ard1.write(b'2')
			
		if data == 3:
			ard.write(('3'.encode()))
			time.sleep(1)
			ard.write(('0'.encode()))
			data = 6
		if data == 4:
			ard.write(('4'.encode()))
			time.sleep(1)
			ard.write(('0'.encode()))
			data = 6
		if data == 0:
			ard.write(('0'.encode()))
		if data == 5:
			ard.write(('5'.encode()))
			time.sleep(1)
			ard.write(('0'.encode()))
			data = 6
		time.sleep(1)
##talk('xin chào tôi là đi seo rô bốt v 3, hân hạnh được giúp đỡ')
if __name__ == "__main__":
    t1 = Thread(target = runA)
    t2 = Thread(target = runB)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:		
        pass


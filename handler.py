import notifier
import recognizer
import os
import cv2 as cv
import time

print("###############################################")
print("Programmer: Flajt")
print("License: GNU General Public License, Version 3")
print("##############################################")



bad_path="/home/pi/Desktop/Pi_Secure/bad_images/"
Id=open("/home/pi/Desktop/Pi_Secure/dataset/ID.txt","r")
Idlist=[]
nameslist=[]
recognizer=recognizer.recognizer("/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml")
notifier=notifier.notyfie()

def main_detection():
	while True:
		IDS, person_found, conf, frame=recognizer.recognize(0)
		if conf>=80.0:
			print(frame)
			print(type(frame))
			#read=cv.imread(str(frame))
			curtime=time.strftime("%d.%m.%Y%H:%M:%S")
			#cv.imwrite(,bad_path+curtime+".txt")
			IDS="Unknown person"
			notifier.sendmail()
			notifier.instapush(curtime)

		print(IDS)
		print("conf "+str(conf))
		for objects in Idlist:
			if str(IDS)==objects:
				print(objects)
				name=nameslist[int(objects)-1]
				print(name)
				
def setup():
	for ids in Id:
		spliter=ids.split(" ")
		name=spliter[0]
		ID=spliter[1].split("\n")
		Idlist.append(ID[0])
		nameslist.append(name)
	main_detection()

setup()

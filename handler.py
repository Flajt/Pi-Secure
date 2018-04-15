import notifier
import recognizer
import os
import cv2 as cv
import time


bad_path="/home/pi/Desktop/Pi_Secure/bad_images/"
Id=open("/home/pi/Desktop/Pi_Secure/dataset/ID.txt","r")
Idlist=[]
nameslist=[]
recognizer=recognizer.recognizer("/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml")
notifier=notifier.notyfie()
try:
	os.chdir("/home/pi/Desktop/Pi_Secure/")
	with open("inform_me.txt","r") as f:
		name=f.read()
		f.close()

except Exception as e:
	setup()

def main_detection():
	os.chdir("/home/pi/Desktop/Pi_Secure/")
	blackliste=[]
	persons=[]
	blacklist=open("blacklist.txt","r")
	for i in blacklist:
		ID_in_black_list=i.split(" ")[1]#check if everything is ok
		person=ID_in_black_list[0]
		persons.append(person)
		blacklist.apppend(ID_in_black_list)

	while True:
		IDS, person_found, conf, frame=recognizer.recognize(0)
		try:
			if conf>=80.0:
				#print(frame)
				#print(type(frame))
				curtime=time.strftime("%d.%m.%Y%H:%M:%S")
				cv.imwrite(bad_path+curtime+".jpg",frame)
				IDS="Unknown person"
				notifier.sendmail()
				notifier.instapush(curtime)
			for i in blackliste:
				if IDS==i:
					curtime=time.strftime("%d.%m.%Y%H:%M:%S")
					cv.imwrite(bad_path+curtime+".jpg",frame)
					notifier.instapush(blacklisted=persons.index(i-1))
					notifier.sendmail(content="A blacklisted person enterd your area! Image below")

			if name==nameslist[IDS-1]:
				curtime=time.strftime("%d.%m.%Y%H:%M:%S")
				cv.imwrite(bad_path+curtime+".jpg",frame)
				notifier.instapush(inform=True, person=name)
				notifier.sendmail(curtime,content="Your notification. A fired arrives")

		except TypeError:
			pass

			#print(IDS)
			#print("conf "+str(conf))

		for objects in Idlist:
			if str(IDS)==objects:
				#print(objects)
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

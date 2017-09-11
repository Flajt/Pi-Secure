import cv2 as cv
import os
import argparse
#import numpy as np
import time

print("##################################################")
print("Programmer: Flajt ")
print("License: GNU General Public License, Version 3 ")
print("##################################################")
name=input("Enter the name of the person: ")#add that every picture in /pos will get named like the person
number=input("Enter an ID number for that person: ")
dire="/home/pi/Desktop/Pi_Secure/pos"
num=0
faceCascade = cv.CascadeClassifier("/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml")
File=open("/home/pi/Desktop/Pi_Secure/dataset/info.csv","w")
os.chdir(dire)


print("Graysacel Images...")
for image in os.listdir(os.getcwd()):
    read=cv.imread(image)
    convert_gray=cv.cvtColor(read, cv.COLOR_BGR2GRAY)
    convert_gray=cv.equalizeHist(convert_gray)
    new=cv.resize(convert_gray, (300, 300))
    cv.imwrite(image, new)
print("Done!")
print("")
print("List all Images...")


for image in os.listdir(os.getcwd()):
    output=cv.imread(image)
    faces = faceCascade.detectMultiScale(output,scaleFactor=1.3,minNeighbors=5,minSize=(45, 45))
    time.sleep(0.2)
    for (x,y,w,h) in faces:
        cv.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cropped=output[int(y):int(y)+int(h), int(x):int(x)+int(w)]
        cv.imwrite("/home/pi/Desktop/Pi_Secure/data/"+number+"."+str(num)+".jpg",cropped)
        num=num+1
    try:
        os.remove(image)
    except Exception:
        pass



    cv.waitKey(1)
    time.sleep(0.5)
    cv.imshow("Note: This Programm is not 100%, correct!" ,output)

os.chdir("/home/pi/Desktop/Pi_Secure/data")
for images in os.listdir(os.getcwd()):
    cur_dir=os.getcwd()
    text=str(cur_dir)+"/"+images+"\n"#+";"+str(direnum) #+" 1"+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n" the seccond # is if you need the face coordinates                    print(text)
    File.write(text)




ID=open("/home/pi/Desktop/Pi_Secure/dataset/ID.txt","a")
ID.write(name+" "+number+"\n")
ID.close()
print("Done!")
File.close()
cv.destroyAllWindows()

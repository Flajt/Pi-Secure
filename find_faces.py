import cv2 as cv
import os
import argparse
import numpy as np
import time


dire="pos"
line=0
faceCascade = cv.CascadeClassifier("D:\DOWNLOADS\opencv\sources\data\haarcascades_GPU\haarcascade_frontalface_default.xml")

for image in os.listdir(dire):
    read=cv.imread("pos/"+image)
    convert_gray=cv.cvtColor(read, cv.COLOR_BGR2GRAY)
    new=cv.resize(convert_gray, (300, 300))
    cv.imwrite("pos/"+image, new)

for image in os.listdir(dire):
    output=cv.imread("pos/"+image)
    faces = faceCascade.detectMultiScale(output,scaleFactor=1.3,minNeighbors=5,minSize=(30, 30))
    for (x,y,w,h) in faces:
            cv.rectangle(read, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cur_dir=os.getcwd()
            text=str(cur_dir)+"/"+"pos/"+image+" 1"+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n"
            File=open("info.txt","a")
            File.write(text)

            cv.waitKey(1)
            time.sleep(0.5)
            cv.imshow("Note: This Programm is not 100%, correct!" ,output)

File.close()

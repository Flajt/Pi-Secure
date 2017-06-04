#!bin/bash/python

import sys
import os
import time
import cv2 as cv
import numpy as np
import urllib


class cam():
    def __init__(self, ip_1, ip_2, cam_number):
        self.ip_1=ip_1
        self.ip_2=ip_2
        self.cam=cam_number


    def cam_connect(self):
        self.cam_path_1=""
        self.cam_1=cv.VideoCapture(self.cam)#link for both cameras has to be inserted here and above
        while True:
            try:
                ret, frame=self.cam_1.read()
            except Exception as e:
                return e

            return True


    def face_detection(self):
        self.picture_path="/home/pi/Desktop/Pi_Secure/picture"
        os.chdir(self.picture_path)
        face_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        eye_cascade=cv.CascadeClassifier("haarcascade_eye.xml")
        cap1=cv.VideoCapture(self.cam)
        while True:
            ret, frame=cap1.read()
            gray=cv.cvtColor(frame, cv.Color_BRG2GRAY) #convert the "frame"(video) color to grey
            faces=face_cascade.detectMultiScale(gray, 1.5, 5)
            for (x,y,w,h) in faces: #x=x coordinate, y=y coordinate , w=width and h=height
                eye_gray=gray[y:y+h, x:x+w] #setup this so I detect the eys in the faces ^^
                eyes=eye_cascade.detectMultiScale(eye_gray)
                if  faces or eyes==True:
                    return True
                else:
                    return False

    def face_check():
        self.picture_path="/home/pi/Desktop/Pi_Secure/picture"
        pass

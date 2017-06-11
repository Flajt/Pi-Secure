#!/bin/bash/python

import Cam
import os

cam=Cam(1)
cam2=Cam(1)
while True:
    back=cam.cam_connect()

    if back==True:
        is_face=cam.face_detection()
        if is_face==True:
            face_check()

    else:
        print("!-------------------!")
        print("An error has occured!")
        print(cam.check)
        print("!--------------------!")
        print("")

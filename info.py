#!bin/bash/python

import cv2 as cv
import numpy as np
import os
import argparse

"""
This Script will search ugly Images like deleted Images or else and
delete them. And it create a info file of a folder your choice
"""


def uglies(dire="neg",):
    """
    This Script search for the "ugly" pictures in your positiv and negativ
    file Directory. Make sure you has only one Image per neg folder.
    """

    for file_type in [dire]:
        for image in os.listdir(file_type): #list all Images in the neg or pos Directory
            for uglies in os.listdir("bad_images/u_"+dire): # a for loop that run for all ugly Images in the Directory
                try:
                    file_path=str(file_type)+"/"+str(image) #the path to the current image/s
                    ugly=cv.imread("bad_images/u_"+dire+"/"+str(uglies))#read the "ugly" image at the current path
                    image=cv.imread(file_path)# read the current image
                    if ugly.shape==image.shape and not (np.bitwise_xor(ugly, image).any()): #checks first if the image in the same dimension and second if the current image and any of the ugly files the same and not diffrent
                        print("[*]: Delete "+str(file_path))
                        os.remove(file_path)


                except Exception as e:
                    print("[!]: An Error ocurred: "+str(e))

#uglies("neg")
#x=input("Wich dir you want to clean up? (pos/neg):")
#uglies(str(x))


def info_text():
    for file_type in ["neg","pos"]:
        for img in os.listdir(file_type):
            if file_type=="neg":
                text=file_type+"/"+img+"\n"
                f=open("bg.txt","a")
                f.write(text)

            elif file_type=="pos":
                text=file_type+"/"+img+"1 0 0 250 250\n"
                File=open("info.txt","a")
                File.write(text)
    print("[*]: Info files are created!")




parser=argparse.ArgumentParser()
parser.add_argument("-r","--run",help="You have to enter the programm you want to run (info=create a info.txt and a bg.txt or clean=search for ugly images in your pos and neg folders)",action="store")
parser.add_argument("-d","--directory",help="The name of the directory. Thats needed for the clean command", action="store")
parser.add_argument("-a","--all",help="Run the clean command for both directorys (neg and pos)",action="store_true")
arg=parser.parse_args()
if arg.run=="info":
    info_text()
if arg.run=="clean" and arg.directory=="neg" or "pos":
    uglies(arg.directory)
    print("\n Checking all directorys done")
if arg.all:
    print("Check neg directory")
    uglies()
    print("Check the pos directory")
    uglies("pos")

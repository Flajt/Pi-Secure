#!bin/bash/python

import urllib.request
import cv2 as cv
import numpy as np
import os
import sys

link_neg="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02958343"#sys.argv[0]
link_pos="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02121620" #sys.argv[1]

neg_urls=urllib.request.urlopen(link_neg).read().decode() # open the url, read it, and decode the bytes
pos_urls=urllib.request.urlopen(link_pos).read().decode()

if not os.path.exists("neg"):
    os.mkdir("neg")
#if not os.path.exists("pos"):
#    os.mkdir("pos")

pic_count_pos=1
pic_count_neg=1

for i in neg_urls.split("\n"): #split the urls and format them; so it split them in diffrent lines
    try:
        print("[*] Url: "+str(i))
        print("[i]: Current Picture Number: "+str(pic_count_neg))
        urllib.request.urlretrieve(i,"neg/"+str(pic_count_neg)+str(".jpg"))# grab url and save it with the name: neg/ and the pic number as .jpg file
        img_neg=cv.imread("neg/"+str(pic_count_neg)+str(".jpg"), cv.IMREAD_GRAYSCALE)
        neg_new=cv.resize(img_neg, (300, 300)) #convert the gray image from above to a 300x300 sized image
        cv.imwrite("neg/"+str(pic_count_neg)+str(".jpg"), neg_new)#write the formated image in the "old" file
        pic_count_neg=pic_count_neg+1


    except Exception as e:
        print("[!] Error:"+str(e))

"""for i in pos_urls.split("\n"):
    try:
        print("[*] Url: "+str(i))
        print("[i]: Current Picture Number: "+str(pic_count_pos))
        urllib.request.urlretrieve(i,"pos/"+str(pic_count_pos)+str(".jpg"))# grab url and save it with the name: pos/ and the pic number as .jpg file
        img_pos=cv.imread("pos/"+str(pic_count_pos)+str(".jpg"), cv.IMREAD_GRAYSCALE)
        pos_new=cv.resize(img_pos, (250, 250)) #convert the gray image from above to a 250x250 sized image
        cv.imwrite("pos/"+str(pic_count_pos)+str(".jpg"), pos_new)#write the formated image in the "old" file
        pic_count_pos=pic_count_pos+1

    except Exception as e:
        print("[!] Error:"+str(e))"""

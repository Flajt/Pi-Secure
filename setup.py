#!/usr/bin/env python

import os

base_path="/home/pi/Desktop/Pi_Secure/"

os.chdir(base_path)
os.mkdir("data")
os.mkdir("key")
os.mkdir("bad_images")
os.mkdir("dataset")
os.mkdir("pictures")
os.mkdir("pos")
os.mkdir("scripts")
os.mkdir("mail")
os.system("sudo pip3 install instapush")
print("Please copy all scripts with .py or .sh in the scripts folder!"

import cv2 as cv
import os
import numpy as np
from PIL import Image

recognizer=cv.face.createLBPHFaceRecognizer()
if not os.path.exists("/home/pi/Desktop/Pi_Secure/dataset"):
	os.chdir("/home/pi/Desktop/Pi_Secure")
	os.mkdir("dataset")

def trainer_create_info():
	faces=[]
	ID=[]

	os.chdir("/home/pi/Desktop/Pi_Secure/pos")

	dataset=open("/home/pi/Desktop/Pi_Secure/dataset/info.csv","r")
	for lines in dataset:
		delete=lines.split("\n")#delete the \n 
		image=Image.open(delete[0]).convert("L")
		array=np.array(image,"uint8")
		line=lines
		first_cut=line.split("\\")[-1]
		second_cut=first_cut.split(".")[0]
		Id=second_cut.split("/")[-1]#cut at the latest / 
		#exit()
		Id=int(Id)
		ID.append(Id)
		faces.append(array)
	return faces, np.array(ID)

#if not os.path.isfile("/home/pi/Desktop/Pi_Secure/dataset/dataset.yml"):
 #       print("Creat new trainings dataset in /home/pi/Desktop/Pi_Secure/dataset/")
  #      faces, names=trainer_create_info()
   #     recognizer.train(faces, names)
    #    recognizer.save("/home/pi/Desktop/Pi_Secure/dataset/dataset.yml")
     #   print("Done!")
#else:
print("Training dataset...")
#recognizer.load("/home/pi/Desktop/Pi_Secure/dataset/dataset.yml")
faces, names=trainer_create_info()
#recognizer.update(faces, names)
#print(faces)
print(names)
recognizer.train(faces, names)
recognizer.save("/home/pi/Desktop/Pi_Secure/dataset/dataset.yml")
print(str(names))
print("Done!")

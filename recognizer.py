import cv2 as cv
import os

class recognizer():
	def __init__(self, cascade_path):
		self.path=cascade_path
		self.classifier=cv.CascadeClassifier(self.path)
		self.Id=0

	def recognize(self, cam):
		conf=None
		recognizer=cv.face.createLBPHFaceRecognizer()
		recognizer.load("/home/pi/Desktop/Pi-Secure/dataset/dataset.yml")
		video=cv.VideoCapture(cam)

		while True:
			ret,frame=video.read()
			gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
			gray = cv.equalizeHist(gray)
			person=self.classifier.detectMultiScale(gray, 1.5, 5)
			person_is_their=False
			self.Id=0
			for (x, y, w, h) in person:
				person_is_their=True
				try:
					self.Id, conf=recognizer.predict(gray[y:y+h, x:x+w])
				except Exception:
					pass
			return self.Id, person_is_their, conf, frame

# add conf !!!
#video.release

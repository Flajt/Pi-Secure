import os
import smtplib
from instapush import Instapush, App
form pushetta import Pushetta
from email import *
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



class notyfie():
	def __init__(self):
		self.sender=open("/home/pi/Desktop/Pi-Secure/mail/mail.txt","r")
		self.sender=self.sender.readline()
		#print(self.sender)
		self.bad_path="/home/pi/Desktop/Pi-Secure/bad_images/"
		self.id_path="/home/pi/Desktop/Pi-Secure/key/"




	def sendmail(self,content="An unknow person entered your area. Picture of him/her below",image=True):
		"""Allow you to send a mail"""

		#content="An unknown person enter your area."+"\n"+"Picture below with his face."
		msg=MIMEMultipart()
		msg["From"]="pysecure1@gmail.com"
		msg["To"]=self.sender
		msg["Subject"]="Security Warning!"

		msg.attach(MIMEText(content,"plain"))

		liste=[]
		for images in os.listdir(self.bad_path):
			liste.append(images)
			print(images)

		image=liste[-1]
		attachment=open(self.bad_path+image,"rb")
		part=MIMEBase("application","octet-stream")
		part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header("Content-Disposition","attachmet; filename= "+image)
		msg.attach(part)

		text=msg.as_string()
		mail=smtplib.SMTP("smtp.gmail.com",587)
		mail.ehlo()
		mail.starttls()
		mail.login("pysecure1@gmail.com","Tomas28-29")
		mail.sendmail("pysecure1@gmail.com",self.sender,text)


	def instapush(self, time,blacklisted=[False,None],inform=[False,None],unkown=False):
		"""Allow you to send an instapush/pushetta messages
		actually it's pushetta"""
		ID=open(self.id_path+"Key.txt","r")
		ID=ID.read()
		Secret=open(self.id_path+"secret.txt","r")
		Secret=Secret.read()
		p=Pushetta(ID)
		#app = App(appid=ID,secret=Secret)
		#if blacklisted==False:
			#app.notify(event_name='Warning', trackers={ 'time': time})
		if unknown==True:
			p.pushMessage(secret,"An unknow person has been detected!")
		elif blacklisted[0]==True:
			p.pushMessage(secret, str(blacklisted[1])+" has been detected. (He is on the Blacklist!)")
			#app.notify(event_name="blacklist",tracker={"Name":blacklisted[1]})
		elif inform[0]==True:
			#app.notify(event_name="Inform_me",tracker{"Person":whitlisted[1]})
			p.pushMessage(secret,str(whitlisted[1])+" has arived.")

import os
import sys
import pickle
import socket
import time
mail_path="/home/pi/Desktop/Pi_Secure/mail/"
picture_path="/home/pi/Desktop/Pi_Secure/pictures/"
Video_path="/home/pi/Desktop/Pi_Secure/video/"
key_path="/home/pi/Desktop/Pi_Secure/key/"
main_path="/home/pi/Desktop/Pi_Secure/"
host="192.168.178.62" #enter your IP here
port=5002 #enter your port here
s=socket.socket()
s.bind((host, port))



print("Server is online at "+host+":"+str(port))

def get_data():
	global host
	global port
	global picture_path
	global Video_path
	global key_path
	name=None
	s.listen(1)
	c ,addr=s.accept()
	print("Connection established to"+str(addr))
	data=c.recv(1024)
	data=data.decode("utf-8")
	dataMessage=data.split(" ", 1)  #split data in command a picture or text Dokument
	command=dataMessage[0]
	#print(command)

	if command=="mail":
		#c.send(str.encode("ok"))
		os.chdir(mail_path)
		mail=open("mail.txt","a")
		Mail=c.recv(1024)
		Mail=Mail.decode("utf-8")
		mail.write(Mail+"\n")
		mail.close()


	elif command=="key":
		#c.send(str.encode("ok"))
		os.chdir(key_path)
		key=open("Key.txt","w")
		Key=c.recv(1024)
		Key=Key.decode("utf-8")
		key.write(Key)
		key.close()


	elif command=="key2":
		#c.send(str.encode("ok"))
		os.chdir(key_path)
		key2=open("secret.txt","w")
		Key2=c.recv(1024)
		Key2=Key2.decode("utf-8")
		key2.write(Key2)
		key2.close()



	elif command=="Image":
		os.chdir(picture_path)
		c.send(str.encode("ok"))
		try:
			name=c.recv(1024)
		except (socket.error, socket.errno, Exception):
			get_data()
		name=name.decode("utf-8")
		picture=open(name,"wb")
		try:
			pic=c.recv(1024)
		except (socket.error, socket.errno):
			get_data()
		while pic:
			picture.write(pic)
			try:
				pic=c.recv(1024)
			except (socket.error, socket.errno, Exception):
				c.close()
				get_data()
			if not pic:
				print("Fertig")
				picture.close()


	elif command=="Del":  #that is the command to delete a picture
		os.chdir(picture_path)
		t=os.listdir()
		print(t)
		if t== []:
			t="Nothing is in this Diretory"
			o=t.encode("utf-8")
			c.send(o)
			c.close()
			get_data()
		try:
			t=str(t)
			o=t.encode("utf-8")
			c.send(o)
			pickname=c.recv(1024)
			Picture=pickname.decode("utf-8")
			print(Picture)
			if Picture=="q":
				c.close()
				get_data()
			else:
				os.remove(Picture)
			check=True
			if check==True:
				c.send(str.encode("True"))
			else:
				c.send(str.encode("False"))
		except Exception:
			get_data()


if socket.error:
	get_data()

while True:
		os.chdir(main_path)
		try:
				text=open("ok.txt","r")#this should check that everything what is important be existent
				if text=="ok":
						get_data()
		except(FileExistsError, FileNotFoundError):
				#print("bad")
				os.chdir("/home/pi/Desktop")
				os.mkdir("Pi_Secure")
				os.chdir("/home/pi/Desktop/Pi_Secure/")
				l=open("ok.txt","w")
				l.write("1")
				l.close()
				os.mkdir("pictures")
				os.mkdir("mail")
				os.mkdir("key")
				get_data()

		get_data()






global c,addr
c.close()

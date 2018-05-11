import os
import sys
import pickle
import socket
import time
mail_path="/home/pi/Desktop/Pi-Secure/mail/"
picture_path="/home/pi/Desktop/Pi-Secure/pictures/"
Video_path="/home/pi/Desktop/Pi-Secure/video/"
key_path="/home/pi/Desktop/Pi-Secure/key/"
main_path="/home/pi/Desktop/Pi-Secure/"
datasets="/home/pi/Desktop/Pi-Secure/dataset/"
host="192.168.178.62" #enter your IP here
port=5002 #enter your port here
s=socket.socket()
s.bind((host, port))
"""
Improve the server_up.sh
"""
print("Server is online at "+host+":"+str(port))
os.chdir(main_path+"scripts")
os.system("sudo ./handler.py")

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
	#print(command) for debugging enable this
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

	elif command=="black":
		try:
			c.send(str.encode("ok"))
			os.chdir(picture_path)
			with open("ID.txt","r") as f:
				data=f.read()
				data=data.split("\n")
				for i in data:
					d=i.split(" ")[0]
				d=str(d)
				c.send(d.encode("utf-8"))
				person_to_list=c.recv(1024).decode("utf-8")
				os.chdir(main_path)
				with open("black.txt","a") as f:
					f.write(person_to_list+"\n")
		except Exception as e:
			get_data()
	elif command=="info":
		try:
			c.send("ok")
			os.chdir()
			os.chdir(datasets)# add information script + handler
			with open("ID.txt","r")as f:
				data=f.read()
				data=data.split("\n")
				for i in data:
					d=i.split(" ")[0]
				d=str(d)
				c.send(d.encode("utf-8"))
			with open("inform_me.txt","w") as f:
				name=s.recv(1024).decode("utf-8")
				f.write(name)
			s.send(str.encode("ok"))
		except Exception as e:
			print("[!]: Error: "+str(e))
			print("")
			print("")
			pass
while True:
	try:
		os.chdir(main_path)
		text=open("ok.txt","r")#this should check that everything what is important be existent
		if text=="1":
			get_data()
	except(Exception):
		os.chdir("/home/pi/Desktop")
		os.mkdir("Pi_Secure")
		os.chdir("/home/pi/Desktop/Pi-Secure/")
		l=open("ok.txt","w")
		l.write("1")
		l.close()
		get_data()






global c,addr
c.close()

import os
import sys
import pickle
import socket
import time
mail_path="/home/pi/Desktop/Pi_Secure/mail"
picture_path="/home/pi/Desktop/Pi_Secure/picture"
Video_path="/home/pi/Desktop/Pi_Secure/video"
key_path="/home/pi/Desktop/Pi_Secure/key"
main_path="/home/pi/Pi_Secure"
host="192.168.178.45"
port= 5001
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

    if command=="mail":
        os.chdir(mail_path)
        mail=open(mail_path,"wb")
        Mail=c.recv(1024)
        while Mail:
            mail.write(Mail)
            Mail=c.recv(1024)
            if not mail:
                mail.close()
                break





    if command=="key":
        os.chdir(key_path)
        key=open(key_path,"wb")
        Key=c.recv(1024)
        while Key:
            key.write(Key)
            Key=c.recv(1024)
            if not key:
                key.close()
                break


    if command=="picture":
        os.chdir(picture_path)
        picture=open(picture_path,"wb")
        pic=c.recv(1024)
        while pic:
            picture.write(pic)
            pic=c.recv(1024)
            if not pic:
                c.send("ok")
                picture.close()
                break



    if command=="Del":
        try:
            t=os.listdir()
        except OSError:
            t="Nothing is in this Diretory"
            o=t,encode("utf-8")
            c.send(o)
            c.close()
        o=t.encode("utf-8")
        c.send(o)
        pickname=c.recv(1024)
        Picture=pickname.decode("utf-8")
        os.remove(Picture)
        c.send(str.encode("True"))


if socket.error:
    get_data()

while True:
    if os.path.exists(main_path):      #this should check that everything what is important be existent
        get_data()



    else:
        os.chdir("/home/pi/Desktop")
        os.mkdir("Pi_Secure")
        os.chdir("/home/pi/Desktop/Pi_Secure/")
        os.mkdir("pictures")
        os.mkdir("mail")
        os.mkdir("key")
        get_data()


global c,addr
c.close()

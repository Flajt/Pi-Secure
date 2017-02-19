import os
import sys
import pickle
import socket
import threading
mail_path="/home/pi/Desktop/Pi_Secure/mail"
picture_path="/home/pi/Desktop/Pi_Secure/picture"
Video_path="/home/pi/Desktop/Pi_Secure/video"
key_path="/home/pi/Desktop/Pi_Secure/key"
main_path="/home/pi/Pi_Secure"


def get_data():
    mail_path="/home/pi/Desktop/mail"
    picture_path="/home/pi/Desktop/picture"
    Video_path="/home/pi/Desktop/video"
    global key_path
    name=None
    host="192.168.178.62"
    port= 5001
    s=socket.socket()
    s.bind((host,port))
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
        mail.close()





    if command=="key":
        os.chdir(key_path)
        key=open(key_path,"wb")
        Key=c.recv(1024)
        while Key:
            key.write(Key)
            Key=c.recv(1024)
        key.close()



    if command=="picture":
        os.chdir(picture_path)
        picture=open(picture_path,"wb")
        pic=c.recv(1024)
        while pic:
            picture.write(pic)
            pic=c.recv(1024)
        picture.close()


    if command=="Del":
        os.chdir(picture_path)
        t=os.listdir()
        o=t.encode("utf-8")
        c.send(o)
        pickname=c.recv(1024)
        Picture=pickname.decode("utf-8")
        os.remove(Picture)
        c.send(True)

    else:
        c.send(false)
        get_data()



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

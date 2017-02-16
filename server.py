import os
import sys
import pickle
import socket
import threading
mail_path="/home/pi/Desktop/Pi_Secure/mail"
picture_path="/home/pi/Desktop/Pi_Secure/picture"
Video_path="/home/pi/Desktop/Pi_Secure/video"
key_path="/home/pi/Desktop/Pi_Secure"


def get_data(sock, name):
    mail_path="/home/pi/Desktop/mail"
    picture_path="/home/pi/Desktop/picture"
    Video_path="/home/pi/Desktop/video"
    global key_path
    name=None
    host="192.168.178.22"
    port= 5001

    s=socket.socket()
    filename=sock.recv(2000)
    s.bind()
    if os.path.isfile(filename):
        if filename=="mail.pkl":
            os.chdir(mail_path+"/"+filename)
        else:
            os.chdir(picture_path+"/"+filename)
    elif filename=="mail.pkl":
        os.chdir(mail_path)
    elif filename=="key.pkl":
        os.chdir(key.pkl)
    elif filename=="Del":
        os.chdir(picture_path)
        dirList = os.listdir('.')
        sock.send(dirList)
        picname=sock.recv(1024)
        os.remove(picname)
        sock.send(True)

    else:
        os.chdir(picture_path)




if os.path.exists(mail_path) and os.path.exist(picture_path) and os.path(key_path) exists:
    get_data(sock, name)

else:
    os.chdir("Desktop")
    os.mkdir("Pi_Secure")
    os.chdir("/home/pi/Desktop/Pi_Secure/")
    os.mkdir("pictures")
    os.mkdir("mail")
    os.mkdir("key")
    get_data(sock,name)

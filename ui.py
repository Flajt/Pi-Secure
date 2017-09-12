ok=False
import sys
import socket
import pickle
import os
import time
import getpass
from passlib.hash import pbkdf2_sha256
import cv2 as cv


global x
usern=getpass.getuser()
x=0
password1=False
password2=None
path="C:/Users/"+usern+"/Desktop/pictures/"#these is the folder wich contains the Images wich you can send
cascade_path="D:\DOWNLOADS\opencv\sources\data\haarcascades_GPU\haarcascade_frontalface_default.xml" #Here enter your path to your cascade
curdir=os.getcwd()
print(curdir)
host="192.168.178.62"
port=5002


def get_images():
    image_number=0
    video=cv.VideoCapture(0)
    while True:
        ret, frame=video.read()
        face=cv.CascadeClassifier(cascade_path)
        convert_gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces=face.detectMultiScale(convert_gray ,scaleFactor=1.4 , minNeighbors=5, minSize=(50,50))
        for (x,y,w,h) in faces:
            cv.imwrite(path+"/im_"+str(image_number)+".jpg",frame)
            image_number=image_number+1
        if image_number>=22:
            break
            print("Taking Pictures done!")
            print("You can now send them with the send option!")
            print("")
            print("")
            main()

def Help():                     #help part
    print("")
    print("Help Menue")
    print("-----------")
    print("")
    print("Add picture:")
    print("Add a picture to the Databank")
    print("")
    print("Every person how is not in the Dantabank will create an alarm message ")
    print("If you use it the first time the programm create a picture folder for all pictures.")
    print("If you want to add a picture put it in this folder and run Add picture command number")
    print("Pleas don`t rename the images!")
    print("")
    print("-------------------------------------------------------------------")
    print("Delete picture")
    print("Here you can delete pictures of the Databank so every persons Face you delete will not enter without a alarm message")
    print("")
    print("-------------------------------------------------------------------")
    print("Add mail Adress:")
    print("This option allows you to add a mail adress were the alarm message is going to you can add so many as you like but max. 50")
    print("Only for Premium User")
    print("")
    print("-------------------------------------------------------------------")
    print("For Help:")
    print("Open this Help menue")
    print("")
    print("-------------------------------------------------------------------")
    print("Logout:")
    print("That I dont explain")
    print("")
    print("-------------------------------------------------------------------")
    print("Get Images:")
    print("This runs a programm that capture your face for the face detection")
    print("algorithm. You only need to send this images with the Add picture command.")
    print("")
    print("-------------------------------------------------------------------")
    t=input("Press a button to exit: ")
    if t=="":
        print("")
        print("")
        main()





def addmail():      # add mail function
    global host
    global port

    print("")
    print("Here you can enter another E-Mail adress")
    mail=input("Enter your Mail adress: ")
    check=input("Is that the right adress?[y/n]: "+str(mail)+": ")
    if check=="y":
        s=socket.socket()
        s.connect((host, port))
        s.send(str.encode("mail"))
        traceback=s.recv(1024)
        traceback=traceback.decode("utf-8")
        if traceback=="ok":
            s.send(mail.encode("utf-8"))
            s.close()
            print("")
            print("")
            print("New Mail adress was sended")
            print("")
            print("")
            main()

        elif check=="q":
            print("")
            print("")
            main()

        else:
            print("Something went wrong ")
            print("")
            main()

    else:
        print("")
        print("Enter the correct adress")
        print("")
        addmail()

#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 13: invalid start byte (fix the problem while split the message)

def delpic():                       #the function for delete a picture
    s=socket.socket()
    try:
        s.connect((host, port))
    except socket.error:
        print("")
        print("Could not connect to the server")
        print("")
        main()
    s.send(str.encode("Del"))
    direList=s.recv(2400)
    if direList=="Nothing in this Directory!":
        print("")
        main()
    else:
        print("Here are the picture names:" + direList.decode("utf-8"))
    delete=input("Wich picture do you want to delete: ")
    if delete=="q":
        s.send(str.encode("q"))
        s.close()
        print("")
        main()
    s.send(str.encode(delete))
    ok=s.recv(1024)
    ok=ok.decode("utf-8")
    if ok=="True":
        print("Picture has been deleted")
        o=input("Do you want to continue? [y/n]")
        if o=="y":
            delpic()
        else:
            s.close()
            print("")
            print("")
            main()
    else:
        print("Something goes wrong")
        print("")
        main()






def addpic():           #the add Picture function
    global host
    global port
    check_out=False
    print("Enter the name of the picture")
    print(" ")
    picname=input("Enter the name of the picture: ")
    os.chdir(path)
    if os.path.isfile(picname)==True:
            print("Picture found, move to the next step")
            try:
                s=socket.socket()
                s.connect((host,port))

            except (socket.error):
                print("!------------------------------------------------!")
                print("Could not connect, please check your connection!")
                print("!------------------------------------------------!")
                print("")
                main()
            try:
                command="Image"
                s.send(command.encode("utf-8"))
                back=s.recv(1024)
                back=back.decode("utf-8")
                if back=="ok":
                    print("Picture will send to the server")
                    s.send(str.encode(picname))# send picturename to the server
                    with open(picname,"rb") as f:
                        chunk=f.read(1024)
                        while chunk:
                            s.send(chunk)
                            chunk=f.read(1024)
                            if not chunk:
                                print("Your picture has been send")
                                f.close()
                                answer=input("Do you wish to send another pic? [y/n]: ")
                                if answer=="y":
                                    s.close()
                                    addpic()

                                else:
                                    #f.close()
                                    print("")
                                    s.close()
                                    check_out=False
                                    main()
                else:
                    print("")
                    print("!-----------------------------------------------------!")
                    print("Something goes wrong, maybe the command is not working")
                    print("!-----------------------------------------------------!")
                    print("")
                    main()

            except socket.error:
                print("")
                print("!-------------------------------------------------------------!")
                print("Could not connect to the server. Please check your Connection!")
                print("!-------------------------------------------------------------!")
                print("")
                main()

            back=s.recv(1024)
            back=back.decode("utf-8")
            if back=="ok":
                print("Image has been sucsessfully sended!")
            else:
                print("")
                print("!--------------------!")
                print("Image was not sended!")
                print("Check your Connection")
                print("!--------------------!")
                print("")
                main()
                m=input("Do you want to continue? [y/n] ")
            if m=="y":
                addpic()
            else:
                print("")
                print("")
                s.close()#close Connection
                main()

    else:
        print("The file could not found try it aggain")
        q=input("Do you want to continue? [y/n]")
        if q=="y":
            print("")
            addpic()
        if q=="n":
            print("")
            try:
                s.close()
            except Exception:
                pass
            main()





def main():         #main part with options
    global user
    global passw
    print("1:Add picture")
    print("2:Delete picture")
    print("3:Add mail Adress")
    print("4:For help")
    print("5:For logout")
    print("6:Get Images")
    wish=int(input("What do you want to do?: "))
    try:
        if wish==1:
            addpic()
        elif wish==2:
            delpic()
        elif wish==3:
            addmail()
        elif wish==4:
            Help()
        elif wish==5: #error fixed something with the closing process was wrong
            sys.exit()
            exit()
        elif wish==6:
            get_images()
        else:      #capture much errors to prevent a not valid input
            print("")
            print("!----------------!")
            print("Not valid input!")
            print("!---------------!")
            print
            main()
    except Exception as e :
        print("")
        print("")
        main()



def create():                           #the funktion were the user add his information
    global password1
    global password2
    global hash
    global host
    global port
    Pass_ok=False   #add all important infos
    user=input("Create a Username: ")
    print("Welcome "+user)
    username=open("username.pkl", "wb")
    save=pickle.dump(user,username)
    while password1!=password2:
        password1=input("Enter your Password: ")
        password2=input("Confirm your Password: ")
        Pass_ok=True

    if Pass_ok==True:
        hash = pbkdf2_sha256.encrypt(password2, rounds=200000, salt_size=16)
        password=open("pass.pkl","wb")
        save2=pickle.dump(hash, password)


    mail=input("Enter your Mail adress:")   #more important infos
    key=input("Enter your Instapush appid: ")   #the appid
    secret=input("Enter your Instapush secret: ")  #the secret
    password=open("pass.pkl","wb")
    key2=open("Key.pkl","wb")
    username.close()
    password.close()
    s=socket.socket()
    s.connect((host,port))
    s.send(str.encode("mail"))
    time.sleep(0.1)
    s.send(mail.encode("utf-8"))
    s.close()
    s=socket.socket()
    s.connect((host, port))
    s.send(str.encode("key"))
    time.sleep(0.1)
    s.send(key.encode("utf-8"))
    s.close()
    s=socket.socket()
    s.connect((host, port))
    s.send(str.encode("key2"))
    time.sleep(0.1)
    s.send(secret.encode("utf-8"))
    s.close()

    print("")
    main()




def login():    #is the login menue
    global x
    global hash
    while x!=3:
        Pass=input("Enter your Password: ")
        right=pbkdf2_sha256.verify(Pass, hash)
        print(right)
        if right==True:
            print("#########################################################")
            print("Programmer: Flajt")
            print("License: License: GNU General Public License, Version 3")
            print("#########################################################")
            print("")
            print("Welcome back "+user)
            print("")
            main()

        if right==False:
            x=x+1

            if x==3:
                print("That goes Wrong...")
                exit()
                sys.exit()

try:
    hash=pickle.load(open("pass.pkl","rb"))               #this is the part were everything Load dont know if that is working
    user=pickle.load(open("username.pkl","rb"))
    ok=True
except(FileExistsError, FileNotFoundError, EOFError):
    print("!-------------!")
    print("Loading Error")
    print("!------------!")
    print("")
    create()



if ok==True:    #check if all is working
    login()

else:
    print("!----------!")
    print("Load error") # this is the error if the file cant Load
    print("!---------!")
    exit()
    sys.exit()

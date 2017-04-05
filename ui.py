ok=False
import sys
import socket
import pickle
import os
import time
import getpass
from passlib.hash import pbkdf2_sha256
global x
usern=getpass.getuser()
x=0
password1=False
password2=None
path="C:/Users/"+usern+"/Desktop/pictures/"
curdir=os.getcwd()
print(curdir)
host="192.168.178.62"
port=5001


def Help():                     #help part
    print("")
    print("Help Menue")
    print("-----------")
    print("")
    print("Add picture:")
    print("Add a picture to the Databank")
    print("The picture should be a picture from a persons Face how can enter without warning")
    print("Every person how is not in the Dantabank will create an alarm message ")
    print("If you use it the first time the programm create a picture folder for all pictures.")
    print("If you want to add a picture put it in this folder and rund Addpicture")
    print("Pleas name the pictures like the person who is on the picture ")
    print("")
    print("-------------------------------------------------------------------")
    print("Delete pciture")
    print("Here you can delete pictures of the Databank so every persons Face you delete will not enter without a alarm message")
    print("")
    print("-------------------------------------------------------------------")
    print("Add mail Adress:")
    print("This option allows you to add a mail adress were the alarm message is going to you can add so many as you like but max 50")
    print("")
    print("-------------------------------------------------------------------")
    print("For Help:")
    print("Open this Help menue")
    print("")
    print("-------------------------------------------------------------------")
    print("Logout:")
    print("That I dont explain")
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
            print(mail)
            s.close()
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

#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 13: invalid start byte

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
    print("Here are the picture names:" + direList.decode("utf-8"))
    if direList=="Nothing in this Directory!":
        print("")
        main()
    delete=input("Wich picture do you want to delete: ")
    if delete=="q":
        s.close()
        print("")
        main()
    s.send(str.encode("delete"))
    ok=s.recv(1024)
    if ok=="True":
        print("Picture is Deleted")
        o=input("Do you want to continue? [y/n]")
        if o=="y":
            delpic()
        else:
            s.close()
            main()
    else:
        print("Something goes wrong")
        print("")
        main()






def addpic():           #the add Picture function
    global host
    global port
    print("Enter the name of the picture")
    print(" ")
    try:
        t=os.chdir(path)    #test if the dir exist
    except OSError:
        print("error")
        t=False
    if t==False:
        os.chdir("C:/Users/"+usern+"/Desktop")
        os.mkdir("pictures")
        print(os.getcwd())
    print(os.getcwd())
    picname=input("Enter the picture name: ")
    try:
        os.chdir(path)
        os.path.isfile(picname)
    except( FileExistsError, FileNotFoundError, Exception):
        print("The file could not found try it aggain")
        q=input("Do you want to continue? [y/n]")
        if q=="y":
            addpic()
        if q=="n":
            print("")
            s.close()
            main()

    print("Picture found, Data will send pls wait...")
    try:
        s=socket.socket()
        s.connect((host,port))
    except socket.error:
        print("!------------------------------------------------!")
        print("Could not connect, please check your connection!")
        print("")
        main()
    try:
        command="Image"
        s.send(str.encode("Image"))
        time.sleep(1)
        s.send(str.encode(picname))# send picname to the server
        with open(picname,"rb") as f:
            chunk=f.read(1024)
            while chunk:
                s.send(chunk)
                chunk=f.read(1024)
                print(chunk)
                if not chunk:
                    print("fertig")
                    f.close()

    except socket.error:
        print("Could not connect to the server. Please check your Connection!")
    back=s.recv(1024)
    back=back.decode("utf-8")
    if back=="ok":
        print("Image has been sucsessfully sended!")
    else:
        print("image was not sended!")
        print("Check your Connection")
    m=input("Do you want to continue? [y/n]")
    if m=="y":
        addpic()
    if m=="n":
        print("")
        print("")
        s.close()#close Connection
        main()




def main():         #main part with options
    global user
    global passw
    print("1:Add picture")
    print("2:Delete picture")
    print("3:Add mail Adress")
    print("4:For help")
    print("5:For logout")
    wish=int(input("What do you want to do?: "))
    if wish==1:
        addpic()
    if wish==2:
        delpic()
    if wish==3:
        addmail()
    if wish==4:
        Help()
    if wish==5:
        time.sleep(1)
        sys.exit()
        exit()
    if (KeyboardInterrupt, ValueError, Exception):      #capture much errors to prevent a not valid input
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

    if Pass_ok:
        hash = pbkdf2_sha256.encrypt(password2, rounds=200000, salt_size=16)
        password=open("pass.pkl","wb")
        save2=pickle.dump(hash, password)


    mail=input("Enter your Mail adress:")   #more important infos
    key=input("Enter your Instapush appid: ")   #the appid
    secrect=input("Enter your Instapush secret: ")  #the secret
    password=open("pass.pkl","wb")
    key2=open("Key.pkl","wb")
    username.close()
    password.close()
    s=socket.socket()
    s.connect((host,port))
    s.send(str.encode("mail"))
    s.send(mail.encode("utf-8"))
    s.close()
    print("")
    main()




def login():    #is the login menue
    global x
    global hash
    while x!=3:
        Pass=input("Enter your Password: ")
        right=pbkdf2_sha256.verify(Pass, hash)
        if right==True:
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
    print("Loading Error")
    create()



if ok==True:    #check if all is working
    login()

else:
    print("Load error") # this is the error if the file cant Load
    exit()
    sys.exit()

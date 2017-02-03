ok=False
import sys
import pickle
import os
from passlib.hash import pbkdf2_sha256
global x
x=0
password1=False
password2=None
path="/Desktop"
curdir=os.getcwd()
print(curdir)

def create():
    global password1
    global password2
    global hash
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
        save2=pickle.dump(password, hash)
        main()


    mail=input("Enter your Mail adress:")   #more important infos
    password=open("pass.pkl","wb")
    mail2=open("mail.pkl","wb")
    save2=pickle.dump(password,var)
    save3=pickle.dump(mail,mail2)
    fileObject.close()
    password.close()

def login():
    global x
    while x!=3:
        Pass=input("Enter your Password: ")
        right=pbkdf2_sha256.verify(Pass, hash)
        if right==True:
            print("Welcome back "+user)
            main()
        else:
            x=x+1
        if x==3:
            print("That goes Wrong...")
            exit()
            sys.exit()

try:
  hash=pickle.load(open("pass.pkl","rb"))               #this is the part were everything Load dont know if that is working
  user=pickle.load(open("fileObejct.pkl","rb"))
  mail=pickle.load(open("mail.pkl","rb"))
  ok=True
  print(hash)
except:
    print("Loading Error")
    create()

def login():
    passw=open("pass.pkl",)
    user=open("fileObejct.pkl")
    print(user)
    while x!=3:
        passw2=input("Enter your Password: ")
        if pasw==passw2:
            main()
        else:
            x=x+1
    if x==3:
        print("That goes wrong try it later")
        import sys
        sys.exit()
        exit()




if ok==True:    #check if all is working
    login()

else:
    print("Load error") # this is the error if the file cant Load
    exit()
    sys.exit()




def main():         #main part with options
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
        passw.close()
        user.close()
        time.sleep(1)
        sys.exit()
        exit()

def Help():
    print("Help Menue")
    print("-----------")
    print("")
    print("Add picture:")
    print("Add a picture to the Databank")
    print("The picture should be a picture from a persons Face how can enter without warning")
    print("Every person how is not in the Dantabank will create an alarm message")
    print("")
    print("-------------------------------------------------------------------")
    print("Delete pciture")
    print("Here you can delete pictures of the Databank so every persons Face you delete will not enter without /n a alarm message")
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
    print("That i will dont explain")
    t=input("Press a button to exit: ")
    if t=="":
        main()

def addpic():
    print("Enter the name of the picture")
    print("If you use that the first time pls add a folder on your Desktop and put every Picture in that ")
    picname=input("Enter the picture name")
    try:
        t=open(pciname,"r")
    except( FileExistsError, FileNotFoundError):
        print("The file could not found try it aggain")
    if t==True:
        print("Picture found Data will send pls wait...")

    else:
        while t!=open:
            picname=input("Enter the pictures name: ")
            t=open(picname, "r")

ok=False
import sys
import pickle
from passlib.hash import pbkdf2_sha256

def login():
    while x!=3:
        Pass=input("Enter your Password: ")
        right=pbkdf2_sha256.verify(Pass, hash)
        if right==True:
            print("Welcome back"+user)
            main()
        else:
            x=x+1
        if x==3:
            print("That goes Wrong...")
            exit()
            sys.exit()

try:
  hash=open("pass.pckl","r")               #this is the part were everything Load dont know if that is working
  user=open("fileObejct.pckl","r")
  mail=open("mail.pckl","r")
  ok=True


  passw=open("pass.pckl","r")
  user=open("fileObejct.pckl","r")
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

Pass_ok=False   #add all important infos get an error here why?
user=input("Create a Username: ")
print("Welcome"+user)
fileObject = open("username.pckl",'w')
save=pickle.dump(user,fileObject)
while password1!=password2:
    password1=input("Enter your Password: ")
    password2=input("Confirm your Password: ")
    Pass_ok=True

if Pass_ok:
    hash = pbkdf2_sha256.encrypt(password2, rounds=200000, salt_size=16)
    password=open("pass.pckl","w")
    save2=pickle.dump(password,hash)


mail=input("Enter your Mail adress:")
password=open("pass.pckl","w")
mail2=open("mail.pckl","w")
save2=pickle.dump(password,hash)
save3=pickle.dump(mail,mail2)
fileObject.close()
password.close()

if ok==True:    #check if all is working
    login()

else:
    print("Load error") # this is the error if the file cant Load
    exit()
    sys.exit()




def main():         #main part with options
    print(1:Add picture)
    print(2:Delete picture)
    print(3:Add mail Adress)
    print(4:For help)
    print(5:For logout)
    wish=int(input("What do you want to do?: "))
    if wish==1:
        addpic()
    if wish==2:
        delpic()
    if wish==3:
        addmail()
    if wish==4:
        Help()
    if wish==5()
        passw.close()
        user.close()
        time.sleep(1)
        sys.exit()
        exit()

def addpic:

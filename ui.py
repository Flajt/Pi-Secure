try:
  passw=open("pass.pckl","r")
  user=open("fileObejct.pckl,"r")
  print(user)
  while x!=3:
      passw2=input("Enter your Password: ")
      if pasw==passw2:
            main()
      else:
            x=x+1
  if x==3:
            print(That goes wrong try it later)
            import sys
            sys.exit()
            exit()

import pickle
a=input("Create a Username: ")
print("Welcome"+a)
fileObject = open("username.pckl",'wb')
save=pickle.dump(a,fileObject)
while password1!=password2:
  password1=input("Enter your Password: ")
  password2=input("Confirm your Password: ")
  password=open("pass.pckl","wb")
 save2=pickle.dump(password,password2)
 fileObject.close()
 password.close()

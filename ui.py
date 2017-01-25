try:
  passw=open("pass.pckl","r")
  user=open("fileObejct.pckl,"r")
  


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

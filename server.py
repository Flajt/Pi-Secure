import socket
import os
mail_path="/Desktop/mail"
picture_path="/Desktop/picture"
Video_path="/Desktop/video"



# a server script dont know what it does ; )
server_ip="192.168.12"
port=" "

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

test=socket.fromshare(1240)

if test=="mail.pkl":
    os.mkdir(mail_path)

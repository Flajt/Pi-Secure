import socket
import os

# a server script dont know what it does ; )
server_ip="192.168.12"
port=" "

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

mail=socket.fromshare(info=1)

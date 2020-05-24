# sender.py
# Send a file using UDP and verifying the identity using checksum (md5), by calling another scripts.

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM) # AF_INET = IPV4 , SOCK_DGRAM = UDP
host = sys.argv[1] # The ip that was given as an argument
port = 9999
buf = 1024 # Maximum bytes to send
addr = (host,port) # Address to send ip + port

file_name=sys.argv[2]

# Opens file to read in bytes and sending them to the destination
s.sendto(file_name,addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print "Sending ..."
        data = f.read(buf)
s.close()
f.close()

sys.argv = ['md5_check.py', file_name]
execfile('md5_check.py') # Check md5 checksum of the local file
execfile('md5_reciever_from_B.py') # Listen for data of the incoming md5 checksum file from B
execfile('md5_compare.py') # Compare local md5 checksum and md5 checksum from B

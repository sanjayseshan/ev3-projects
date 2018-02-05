# Echo client program
import socket
import sys,time

while True:
 HOST = 'pm-set01.local'    # The remote host
 PORT = 50007              # The same port as used by the server
 s = None
 for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
     af, socktype, proto, canonname, sa = res
     try:
         s = socket.socket(af, socktype, proto)
     except socket.error as msg:
         s = None
         continue
     try:
         s.connect(sa)
     except socket.error as msg:
         s.close()
         s = None
         continue
     break
 if s is None:
     print 'could not open socket'
     sys.exit(1)
 s.sendall('Hello, world')
 data = s.recv(1024)
 print 'Received', repr(data)
 time.sleep(1)
 s.close()


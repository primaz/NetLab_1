#https://docs.python.org/3/library/telnetlib.html

import getpass
import sys
import telnetlib

HOST = "192.168.100.119"
user =  'cisco\n'.encode() #input("Enter your remote account: ")
password = 'cisco\n'.encode() #getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout=1)

tn.read_until("Username: ".encode())
tn.write(user)
tn.write(password)

tn.write("terminal length 0\n".encode())
tn.write("enable\n".encode())
tn.write("cisco\n".encode())
tn.write("conf ter\n".encode())
tn.write("int loop 0\n".encode())
tn.write("ip address 1.1.1.1 255.255.255.255\n".encode())
tn.write("end\n".encode())
tn.write("show ip int brief\n".encode())
tn.write("exit\n".encode())

print(tn.read_all().decode('ascii'))

tn.close()

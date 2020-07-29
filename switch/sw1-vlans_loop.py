#!/usr/bin/env python
#https://docs.python.org/3/library/telnetlib.html

import getpass
import sys
import telnetlib

HOST = "192.168.100.99"
user =  'misael\n'.encode() #input("Enter your remote account: ")
password = 'cisco\n'.encode() #getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout=3)

tn.read_until("Username: ".encode())
tn.write(user)
tn.write(password)

tn.write("conf ter\n".encode())
for i in range(2,21):
    command = "vlan " + str(i) + "\n"
    description = "name Python_VLAN_" + str(i) + "\n"
    tn.write(command.encode())
    tn.write(description.encode())
    tn.write("exit\n".encode())

tn.write("end\n".encode())
tn.write("terminal length 0\n".encode())
tn.write("wr\n".encode())

tn.write("show vlan\n".encode())

print(tn.read_all().decode('ascii'))

tn.close()

#https://docs.python.org/3/library/telnetlib.html

import getpass
import sys
import telnetlib

HOST = "192.168.100.119"

user = 'misael\n'.encode()
#user =  (input("Enter your remote account: ") + "\n")
#user = user.encode()
password = getpass.getpass() + "\n"
password = password.encode()

tn = telnetlib.Telnet(HOST, timeout=1)

tn.read_until("Username: ".encode())
tn.write(user)
tn.write(password)

tn.write("terminal length 0\n".encode())
tn.write("enable\n".encode())
tn.write("cisco\n".encode())
tn.write("conf ter\n".encode())
tn.write("router ospf 1\n".encode())
tn.write("network 0.0.0.0 255.255.255.255 area 0\n".encode())
tn.write("end\n".encode())
tn.write("wr\n".encode())
tn.write("show ip protocols\n".encode())
tn.write("exit\n".encode())

print(tn.read_all().decode('ascii'))

tn.close()

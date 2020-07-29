#https://docs.python.org/3/library/telnetlib.html

import getpass
import sys
import telnetlib

HOST = "192.168.100.99"
user =  'misael\n'.encode() #input("Enter your remote account: ")
password = 'cisco\n'.encode() #getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout=1)

tn.read_until("Username: ".encode())
tn.write(user)
tn.write(password)

tn.write("terminal length 0\n".encode())
tn.write("enable\n".encode())
tn.write("cisco\n".encode())
tn.write("conf ter\n".encode())
tn.write("vlan 2\n".encode())
tn.write("name Python_VLAN_2\n".encode())
tn.write("exit\n".encode())
tn.write("vlan 3\n".encode())
tn.write("name Python_VLAN_3\n".encode())
tn.write("exit\n".encode())
tn.write("vlan 4\n".encode())
tn.write("name Python_VLAN_4\n".encode())
tn.write("exit\n".encode())
tn.write("vlan 5\n".encode())
tn.write("name Python_VLAN_5\n".encode())
tn.write("exit\n".encode())
tn.write("vlan 6\n".encode())
tn.write("name Python_VLAN_6\n".encode())
tn.write("end\n".encode())
tn.write("show vlan\n".encode())

print(tn.read_all().decode('ascii'))

tn.close()

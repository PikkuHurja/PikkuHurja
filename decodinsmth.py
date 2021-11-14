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

inpass = lines[0]
inuser = lines[1]
inport = lines[2]
inhost = lines[3]

inpass = inpass.encode("ascii")
inuser = inuser.encode("ascii")
inport = inport.encode("ascii")
inhost = inhost.encode("ascii")

inpass = b64.b64decode(inpass)
inuser = b64.b64decode(inuser)
inport = b64.b64decode(inport)
inhost = b64.b64decode(inhost)

pw = inpass.decode("ascii")
us = inuser.decode("ascii")
pr = inport.decode("ascii")
hs = inhost.decode("ascii")


if pr.isdigit() == True:
    pr = int(pr)
else:
    pr = 22



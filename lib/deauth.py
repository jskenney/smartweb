#!/usr/bin/python3 -B

# Import Required Libraries
import os, uuid
from smartconfig import authMapFile, cookieName, defaultPage
from tools import loadDB, saveDB
from sessions import Session

# Create a default UUID
myuuid = str(uuid.uuid4())

# Either add that UUID as the cookie (cookieName) or replace myuuid
# with the value of myuuid if it exists
if not 'HTTP_COOKIE' in os.environ:
    print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')
else:
    hc = os.environ['HTTP_COOKIE'].split(';')
    found = False
    for c in hc:
        c = c.strip().split('=')
        if c[0] == cookieName:
            myuuid = c[1]
            found = True
            print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')
    if not found:
        print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')

# Load the user file
userMap = loadDB(authMapFile, {})

# Remove the user from the cookie to username map
if myuuid in userMap:
    del(userMap[myuuid])
    saveDB(authMapFile, userMap)

# Set the user to unknown
user = ''
admin = False
permissions = {}
session = Session(cookieName=myuuid)

print('Content-type: text/html\n\n')
print('<head><meta http-equiv="Refresh" content="0; URL='+defaultPage+'" /></head>')

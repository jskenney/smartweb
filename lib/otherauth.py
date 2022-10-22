# Use this library if you want to leverage
# this system for other web programs

# Import Required Libraries
import os, uuid
from smartconfig import authFile, authMapFile, cookieName
from tools import loadDB

user = ''
permissions = {}

if 'HTTP_COOKIE' in os.environ:
    hc = os.environ['HTTP_COOKIE'].split(';')
    found = False
    for c in hc:
        c = c.strip().split('=')
        if c[0] == cookieName:
            myuuid = c[1]
            found = True
    if found:
        userMap = loadDB(authMapFile, {})
        if myuuid in userMap:
            user = userMap[myuuid]
            userFile = loadDB(authFile, {user:{}})
            permissions = userFile[user]



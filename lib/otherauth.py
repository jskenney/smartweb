# Use this library if you want to leverage
# this system for other web programs

# Import Required Libraries
import os, uuid
from smartconfig import authFile, authMapDir, cookieName
from tools import loadDB
from sessions import Session

# Create a default UUID
user = ''
admin = False
permissions = {}
myuuid = None
session = None

# Get logged on user's cookie
if 'HTTP_COOKIE' in os.environ:
    hc = os.environ['HTTP_COOKIE'].split(';')
    found = False
    for c in hc:
        c = c.strip().split('=')
        if c[0] == cookieName:
            myuuid = c[1]
            found = True
    if found:
        userMap = loadDB(authMapDir+myuuid+'.json', {'user':''})
        user = userMap['user']

# Load User data from authentication file
if user != '':
    pwdata = loadDB(authFile, {})
    if user in pwdata:
        permissions = pwdata[user]
        if 'admin' in permissions and permissions['admin']:
            admin = True
    else:
        user = ''

# Load session variable
if user != '':
    session = Session(cookieName=myuuid, identifier=user)
else:
    session = Session(cookieName=myuuid)
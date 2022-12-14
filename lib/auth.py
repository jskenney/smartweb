# Import Required Libraries
import os, uuid
from smartconfig import authFile, authMapFile, cookieName
from tools import loadDB
from sessions import Session

# Create a default UUID
myuuid = str(uuid.uuid4())
user = ''
permissions = {}
admin = False
session = None

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

# If the user is valid, return their name
if myuuid in userMap:
    user = userMap[myuuid]

# Load User data from authentication file
pwdata = loadDB(authFile, {'0000':{}})
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
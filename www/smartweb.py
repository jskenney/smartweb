#!/usr/bin/python3 -B

# SmartWeb Version 1.0
# Provides a simple web file protection service

# Load in system libraries
import cgi, sys, os, shutil

# Define path for local configuration files
sys.path.append("../lib")
sys.path.append("../config")

# Load in local configuration files and authenitication
from smartconfig import sourceDir, mimeTypes, errorMsg, fileMAP, defaultPage, logonFile, missingFileProvideDefault, provideDirs, authFile, authMapDir, pyMAP, logonTime
from tools import loadDB, saveDB

# Simple function to provide a file back to the browser
def provideFile(filename, mimeTypes, saveas=''):
    extension = os.path.splitext(filename)[1]
    if saveas != '':
        print('Content-Disposition: attachment; filename="'+saveas+'"')
    if extension in mimeTypes:
        print('Content-type: '+mimeTypes[extension]+'\n')
    else:
        print('Content-Type: application/octet-stream\n')
    sys.stdout.flush()
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            shutil.copyfileobj(f, sys.stdout.buffer)
    sys.exit()

# Simple function to provide an error message to the user
def provideError(filename, message):
    print('Content-type: text/html\n\n')
    with open(filename) as f:
        print(f.read().replace('{message}', message))
    sys.exit()

# Get path variable from the web server
form = cgi.FieldStorage()
p = form.getvalue('path')
l = form.getvalue('smartlogoff')

# If no path is provided use default page
if p is None:
    p = defaultPage

# lets abort if the user added another path (not from the rewrite)
if not isinstance(p, str):
    provideError(errorMsg, 'Failed attempt to modify path.')

# Determine what the real file we want to get is
filename = sourceDir + '/' + p

# If the file is in the fileMAP than provide that file
# without authentication and exit
if os.path.split(filename)[1] in fileMAP:
    provideFile(fileMAP[os.path.split(filename)[1]], mimeTypes)

# Identify the user via the auth library
if l is None:
    from auth import user, myuuid, permissions, admin
else:
    permissions = {}
    admin = False
    from deauth import user, myuuid

# Get Username and Password from the user if provided
usnm = form.getvalue('smartwebEmail')
pswd = form.getvalue('smartwebPassword')
mnow = form.getvalue('smartwebTime')

# If username and password were provided, check to see
# if this is a valid user
if usnm is not None and pswd is not None and mnow is not None:
    print('Content-type: text/html\n\n')
    from hashlib import sha256
    from time import time
    pwdata = loadDB(authFile, {})
    usnmhash = sha256(usnm.encode()).hexdigest()
    if not usnmhash in pwdata or 'password' not in pwdata[usnmhash]:
        print("{'message':'invalid password'}")
        sys.exit()
    combined = mnow + pwdata[usnmhash]['password']
    passhash = sha256(combined.encode()).hexdigest()
    if not passhash == pswd or abs(float(mnow)-time()) > logonTime:
        print("{'message':'invalid password'}")
        sys.exit()
    userMap = loadDB(authMapDir+myuuid+'.json', {'user':'', 'start': 0, 'env': ''})
    userMap['user'] = usnmhash
    userMap['start'] = float(mnow)
    userMap['env'] = str(os.environ)[8:-1]
    saveDB(authMapDir+myuuid+'.json', userMap)
    print("{'message':'success'}")
    sys.exit()

# If no user found, then stop
if user == '':
    provideFile(fileMAP[os.path.split(logonFile)[1]], mimeTypes)

# If the file is in the pyMAP than import that file
# and exit the program.  The assumption is that this new script
# will handle the headers and content.
if os.path.split(filename)[1] in pyMAP and os.path.isfile(pyMAP[os.path.split(filename)[1]]):
    pypath, pyfile = os.path.split(os.path.realpath(pyMAP[os.path.split(filename)[1]]))
    pyfile = os.path.splitext(pyfile)
    sys.path.append(pypath)
    import importlib
    importlib.import_module(pyfile[0])
    sys.exit()

# We should try: filename, filename+index.html
# Provide the file if that path exists and exists within the appropriate path
possibilities = [filename]
if len(filename) > 1 and filename[-1] == '/':
    possibilities.append(filename+'index.html')
for filename in possibilities:
    if os.path.exists(filename) and os.path.isfile(filename):
        authorized = False
        if os.path.realpath(filename).startswith(provideDirs) and os.path.realpath(filename).find('/.') == -1:
            authorized = True
        if authorized:
            provideFile(filename, mimeTypes)

# A Valid file wasn't found, try using the default page
if missingFileProvideDefault:
    filename = sourceDir + '/' + defaultPage
    if os.path.exists(filename) and os.path.realpath(filename).find(sourceDir) == 0:
        provideFile(filename, mimeTypes)

# Otherwise just flag it as an error
provideError(errorMsg, 'File not found: '+p)


#!/usr/bin/python3 -B

# SmartWeb Version 1.0
# Provides a simple web file protection service

# Load in system libraries
import cgi, sys, os, shutil

# Define path for local configuration files
sys.path.append("../lib")
sys.path.append("../config")

# Load in local configuration files and authenitication
from smartconfig import sourceDir, mimeTypes, errorMsg, fileMAP, defaultPage, logonFile, missingFileProvideDefault, provideDirs

# Simple function to provide a file back to the browser
def provideFile(filename, mimeTypes):
    extension = os.path.splitext(filename)[1]
    if extension in mimeTypes:
        print('Content-type: '+mimeTypes[extension]+'\n')
    else:
        print('Content-Type: application/octet-stream\n')
    sys.stdout.flush()
    with open(filename, 'rb') as f:
        shutil.copyfileobj(f, sys.stdout.buffer)
    sys.exit()

# Simple function to provide an error message to the user
def provideError(filename, message):
    print('Content-type: text/html\n\n')
    with open(filename) as f:
        print(f.read().replace('{message}', message))
    sys.exit()

# Get that path variable from the web server
form = cgi.FieldStorage()
p = form.getvalue('path')
l = form.getvalue('smartlogoff')

# If no page provided put in a default
if p is None:
    p = defaultPage

# Determine what the real file we want to get is
filename = sourceDir + '/' + p

# If the file is in the fileMAP than provide that file
# without authentication and exit
if os.path.split(filename)[1] in fileMAP:
    provideFile(fileMAP[os.path.split(filename)[1]], mimeTypes)

# Identify the user via the auth library
if l is None:
    from auth import user
else:
    from deauth import user

# If no user found, then stop
if user == 'x' or user == '':
    provideFile(fileMAP[os.path.split(logonFile)[1]], mimeTypes)

# Provide the file if that path exists and exists within the appropriate path
if os.path.exists(filename) and os.path.isfile(filename):
    authorized = False
    for d in provideDirs:
        if os.path.realpath(filename).find(d) == 0:
            authorized = True
    if authorized:
        provideFile(filename, mimeTypes)
    else:
        provideError(errorMsg, 'File not found: '+p)
elif missingFileProvideDefault:
    filename = sourceDir + '/' + defaultPage
    if os.path.exists(filename) and os.path.realpath(filename).find(sourceDir) == 0:
        provideFile(filename, mimeTypes)
    else:
        provideError(errorMsg, 'File not found: '+p)
else:
    provideError(errorMsg, 'File not found: '+p)

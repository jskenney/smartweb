#!/usr/bin/python3 -B

# SmartWeb Version 1.0
# Provides a simple file protection service

# Load in system libraries
import cgi, sys, os, shutil
from hashlib import md5

# Define path for local configuration files
sys.path.append("../lib")
sys.path.append("../config")

# Load Configurations and tools
from smartconfig import authFile, authMapFile
from tools import loadDB, saveDB
from auth import myuuid

# Get username and password from the web server
form = cgi.FieldStorage()
u = form.getvalue('smartwebEmail')
p = form.getvalue('smartwebPassword')

# This form shouldnt provide any real feedback back
# to the user.
print('Content-type: text/html\n\n')

# If username and password were provided, check to see
# if this is a valid user
if u is not None and p is not None:
    up = u + p
    userhash = md5(up.encode()).hexdigest()
    pwdata = loadDB(authFile, {'0000':{}})
    if userhash in pwdata:
        user = userhash
        umap = loadDB(authMapFile, {})
        umap[myuuid] = userhash
        saveDB(authMapFile, umap)
    print(userhash)

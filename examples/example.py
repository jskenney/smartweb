#!/usr/bin/python3 -B

# Required or suggested libraries
import time, sys, os
from json import dumps

# Add the path for the configuration file and libraries
sys.path.insert(0, '../lib')        # smartweb configuration directory

# Load smartweb permissions and additional tools.
from otherauth import user, permissions, admin
from tools import loadDB

# Start outputting a web page
print('Content-type: text/html\n\n')

# Get fields from the web server
form = cgi.FieldStorage()

# If you tried something like https://localhost/example.py?site=test
site = form.getvalue('site')

print("Welcome", user)
print("Permissions:", permissions)
print("Admin:", admin)
print("Site", site)

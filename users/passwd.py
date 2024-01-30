#!/usr/bin/python3 -B

from hashlib import sha256
from getpass import getpass
from sys import argv
from json import loads, dumps

# Save a dictionary to file
def saveDB(filename, data):
    with open(filename, 'w') as f:
        f.write(dumps(data, indent=2))

# Load a dictionary from json
def loadDB(filename, default):
    try:
        with open(filename) as f:
            return loads(f.read())
    except:
        return default

username = argv[-1]

print('username:', username)

authfile = loadDB('users.json', {})

if username.find('@') != -1:
    password = getpass('password: ')
    usnmhash = sha256(username.encode()).hexdigest()
    pwhash   = sha256(password.encode()).hexdigest()
    pwhash   = pwhash + usnmhash
    pwhash   = sha256(pwhash.encode()).hexdigest()
    usnmhash = sha256(usnmhash.encode()).hexdigest()
    authfile[usnmhash] = {'username':username, 'password':pwhash}
else:
    pwhash = input('passhash: ')
    usnmhash = sha256(username.encode()).hexdigest()
    authfile[usnmhash] = {'password':pwhash}

saveDB('users.json', authfile)

print('user add:', usnmhash)
print('hash add:', pwhash)



#!/usr/bin/python3 -B

from hashlib import md5, sha256
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
password = input('password: ')

pwhash = md5(str(str(sha256(username.encode()).hexdigest())+str(sha256(password.encode()).hexdigest())).encode()).hexdigest()
authfile = loadDB('users.json', {})
authfile[pwhash] = {}
saveDB('users.json', authfile)

print('Added hash:', pwhash)



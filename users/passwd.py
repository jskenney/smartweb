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

authfile = loadDB('users.json', {})

if username.find('@') != -1:
    password = input('password: ')
    pwhash = md5(str(str(sha256(username.encode()).hexdigest())+str(sha256(password.encode()).hexdigest())).encode()).hexdigest()
    usnmhash = md5(str(str(sha256(username.encode()).hexdigest())).encode()).hexdigest()
    authfile[usnmhash] = {'username':username, 'password':pwhash}
else:
    pwhash = input('passhash: ')
    usnmhash = username
    authfile[usnmhash] = {'password':pwhash}

saveDB('users.json', authfile)

print('user add:', usnmhash)
print('hash add:', pwhash)



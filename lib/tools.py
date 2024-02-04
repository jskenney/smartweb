#!/usr/bin/python3 -B

from json import loads, dumps

# Save a dictionary to file
def saveDB(filename, data):
    with open(filename, 'w') as f:
        f.write(dumps(data))

# Load a dictionary from json
def loadDB(filename, default):
    try:
        with open(filename) as f:
            return loads(f.read())
    except:
        return default


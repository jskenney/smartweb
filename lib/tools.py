#!/usr/bin/python3 -B

from json import loads, dumps

# Save a dictionary to file
def saveDB(filename, data, display=False, format=False):
    if display:
        print('# Saving', filename)
    with open(filename, 'w') as f:
        if format:
            f.write(dumps(data, indent=2))
        else:
            f.write(dumps(data))

# Load a dictionary from json
def loadDB(filename, default, display=False):
    if display:
        print('# Loading', filename)
    try:
        with open(filename) as f:
            return loads(f.read())
    except:
        return default

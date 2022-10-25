#!/usr/bin/python3 -B

# The library provides a PHP like SESSIONS capability in Python
# https://realpython.com/inherit-python-dict/
# https://docs.python.org/3/reference/datamodel.html

from os.path import exists
from getpass import getuser
from os import environ, makedirs, chmod
from json import loads, dumps
from uuid import uuid4

# Retrieve the value of the session cookie and/or create the cooking and
# return the identifier.
def cookie(cookieName='smartweb'):

    # Create a default UUID
    myuuid = str(uuid4())

    # Either add that UUID as the cookie (cookieName) or replace myuuid
    # with the value of myuuid if it exists
    if not 'HTTP_COOKIE' in environ:
        print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')
    else:
        hc = environ['HTTP_COOKIE'].split(';')
        found = False
        for c in hc:
            c = c.strip().split('=')
            if c[0] == cookieName:
                myuuid = c[1]
                found = True
                print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')
        if not found:
            print('Set-Cookie: '+cookieName+'='+myuuid+'; Path=/; Secure')
    
    # Return the created or found cookie
    return myuuid

# A Modified dictionary object which loads on first access and
# writes on any update
class Session:
    def __init__(self, cookieName='smartweb', identifier=None):
        if identifier is None:
            identifier = cookie(cookieName)
        self.path = '/tmp/python-sessions-' + getuser() +'/sessions/'
        self.filename = self.path+identifier
        self.data = None
        self.debug = False
    def load(self, default):
        if self.data is None:
            try:
                makedirs(self.path, exist_ok=True)
            except:
                if self.debug:
                    print('# ERROR: Unable to create sessions directory', self.path)
            try:
                chmod(self.path, 0o700)
            except:
                if self.debug:
                    print('# ERROR: Unable to set permissions on sessions directory', self.path)
            try:
                with open(self.filename) as f:
                    if self.debug:
                        print('# Loading', self.filename)
                    self.data = loads(f.read())
            except:
                self.data = default
    def save(self):
        self.load({})
        try:
            with open(self.filename, 'w') as f:
                f.write(dumps(self.data, indent=2))
                if self.debug:
                    print('# Saving', self.filename)
        except:
            if self.debug:
                print('# ERROR Unable to save to', self.filename)

    def __setitem__(self, key, value):
        self.load({})
        self.data[key] = value
        self.save()
    def __getitem__(self, key, owner=None):
        self.load({})
        return self.data[key]
    def __delitem__(self, key):
        self.load({})
        self.data.__delitem_(key)
        self.save()
    def __str__(self):
        self.load({})
        return str(self.data)
    def __repr__(self):
        self.load({})
        return repr(self.data)
    def __contains__(self, key):
        self.load({})
        return key in self.data
    def __iter__(self):
        self.load({})
        return self.data.__iter__()
    def __len__(self):
        self.load({})
        return self.data.__len__()
    def keys(self):
        self.load({})
        return list(self.data.keys())

if __name__ == '__main__':
    a = Session()
    print('Creating First set of values')
    a[5] = {'a':2}
    print('Creating Second set of values')
    a[6] = {'g':5}
    print(a[5])
    print(a[5]['a'])
    print(a.keys()) 
    print(str(a))
    print(repr(a))
    print(5 in a)
    print(6 in a)
    for key in a:
        print(key)
    print(len(a))
    print('Creating Value')
    a['test'] = 3
    print(a)


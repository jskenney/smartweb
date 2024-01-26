
# Base directory
baseDir      = '/var/www/html/smartweb'

# Web Error Message
errorMsg     = baseDir + '/lib/error.html'

# Location of actual web content
sourceDir    = baseDir + '/real/'

# Authorized source directories
provideDirs  = (sourceDir)

# Default webpage
defaultPage  = 'index.html'

# Provide default page when a file is not found?
missingFileProvideDefault = False

# Location of authentication information
userDir      = baseDir + '/users/'

# Location of auth file (username: data)
authFile     = userDir + 'users.json'

# Location of cookie to user mappings
authMapFile  = userDir + 'cookiemap.json'

# Location of login files
loginDir     = baseDir + '/login/'

# Logon File name (add this to the fileMAP below as well)
logonFile    = 'smartweb-logon.html'

# How much time / clock skew to allow between client and server
# For authentication (seconds)
logonTime    = 120

# Directory in which to store session files
sessionDir   = '/tmp/'

# specific MIME types, that will not be default octet-stream
mimeTypes    = {'.html' : 'text/html',
                '.xhtml': 'text/xhtml',
                '.txt'  : 'text/plain',
                '.js'   : 'text/javascript',
                '.css'  : 'text/css',
                '.png'  : 'image/png',
                '.jpg'  : 'image/jpeg',
                '.jpeg' : 'image/jpeg'
               }

# if these files are asked for, with any path, the mapped
# files will be returned instead, these are allowed even
# if the users is not authenticated.  These are meant to
# be used to provide logon pages and supporting files.
fileMAP      = {'smartweb-logon.html' : loginDir + 'smartweb-logon.html',
                'smartweb-logon.css'  : loginDir + 'smartweb-logon.css',
                'smartweb-sha256.js'  : loginDir + 'smartweb-sha256.js',
                'smartweb-icon.png'   : loginDir + 'smartweb-icon.png',
                'smartweb-avatar.png' : loginDir + 'smartweb-avatar.png',
                'smartweb-jquery.js'  : loginDir + 'smartweb-jquery.js',
                'smartweb-signup.html': loginDir + 'smartweb-signup.html'
               }

# if python files are asked for, check the following map of authorized
# python scripts.  If they are not in this dictionary, they will be
# provided as text.  If they are in this, they will be imported, be careful
# on how you add python files.  Just as with the fileMAP, location does
# not matter.
pyMAP        = {'logoff': baseDir + '/lib/deauth.py'}

# Name of the cookie we will store for user tracking
cookieName   = 'smartweb'


# Base directory
baseDir      = '/var/www/html/smartweb'

# Web Error Message
errorMsg     = baseDir + '/lib/error.html'

# Location of actual web content
sourceDir    = baseDir + '/real/'

# Authorized source directories
provideDirs  = [sourceDir]

# Default webpage
defaultPage  = 'index.html'

# Provide default page when a file is not found?
missingFileProvideDefault = True

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

# specific MIME types, that will not be default octet-stream
mimeTypes    = {'.html':'text/html', 
                '.xhtml':'text/xhtml', 
				'.js': 'text/javascript',
				'.css': 'text/css'
			   }

# if these files are asked for, with any path, the mapped
# files will be returned instead, these are allowed even
# if the users is not authenticated.  These are meant to 
# be used to provide logon pages and supporting files.
fileMAP      = {'smartweb-logon.html': loginDir + 'smartweb-logon.html',
				'smartweb-logon.css': loginDir + 'smart-logon.css',
				'smartweb-sha256.js': loginDir + 'smartweb-sha256.js',
				'smartweb-icon.png': loginDir + 'smartweb-icon.png',
				'smartweb-login.css': loginDir + 'smartweb-login.css',
				'smartweb-avatar.png': loginDir + 'smartweb-avatar.png'
			   }

# Name of the cookie we will store for user tracking
cookieName   = 'smartweb'
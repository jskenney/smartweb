# smartweb (yes, a rather bad name...)

Use Apache2's <a href="https://httpd.apache.org/docs/current/mod/mod_rewrite.html">mod_rewrite</a> module and a python script acting as a proxy to protect the contents of web directory.

In simplier terms, the proxy script will exist in within the normal path of the web server, while the protected contents will be stored somewhere else, once a user logs on those external files will be provide as if they existed on the path.

Additionally, this framework provides authentication and the equivalent of PHP Sessions to Python scripts.

# Setup:

- In your apache.conf file, add smartweb.py as a Directory index, example:

~~~
<IfModule dir_module>
    DirectoryIndex index.html index.php index.py smartweb.py
</IfModule>
~~~

- Edit the *.htaccess* file in the web root directory and add something similar to the following (Note: A default .htaccess file is provided in the repo.)

~~~
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /smartweb.py?path=$1 [QSA,L]
~~~

- Make sure the permissions and ownership of the smartweb/users directory is writable by the web users, usually www or www-data.

- Edit the configuration file by renaming smartconfig-example.py to smartconfig.py in the /lib directory setting all required paths

- Create a user that can log on via *passwd.py* script in users.
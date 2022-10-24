# smartweb 

Use Apache2's <a href="https://httpd.apache.org/docs/current/mod/mod_rewrite.html">mod_rewrite</a> module and a python script acting as a proxy to protect the contents of web directory.

In simplier terms, the proxy script will exist in within the normal path of the web server, while the protected contents will be stored somewhere else, once a user logs on those external files will be provide as if they existed on the path.


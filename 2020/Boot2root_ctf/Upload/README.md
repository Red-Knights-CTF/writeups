
![](https://i.imgur.com/nEQGpLG.png)
# Upload(web)

url : http://198.211.100.125:8080/upload.php

After every hit-end trial method of uploading php code with different extensions. file Upload successfully with different php extensions (`php2, .php3, .php4, .php5, .php6, .php7, .phps, .pht, .phtml, .pgif, .shtml, .htaccess, .phar, .inc`) but code not work.


may be it is due to the **.htaccess protection**.

and this **upload.php** file always **overwrite** the existing file during uploading in directory.

so i decided to change the content **under .htaccess**.

than i make a **.htaccess** file with configuration.
    
    ```AddType application/x-httpd-php .png```
    
The above configuration would instruct the Apache HTTP Server to execute PNG images as though they were PHP scripts

**.htaccess** uploading success(hurray .htaccess file overwrited with our conf)![](https://i.imgur.com/uMZ2t4N.png)
![](https://i.imgur.com/d7Xb2qq.png)


----
lets upload the php code with .png extension and donot forgot to change content-type in burpsuite while uploading
 

```Content-Type: application/x-httpd-php```


![](https://i.imgur.com/O8qUA5D.png)
![](https://i.imgur.com/YCCEPmJ.png)
![](https://i.imgur.com/gXWMuCT.png)

# flag : b00t2root{remote_code_execution_vulnerability} 

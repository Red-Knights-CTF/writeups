#  everyone intrested in my secret life ( ᴗ )

**Category**: Crypto \
**Points**: 150

## Discription

> I Know you want to know the secrets of my life but it is not that much easy. I can only provide you some help you have to figure out it.

## Solution

We are given `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3liZXJncmFic3tOMHRfVDAwXzM0c1l9In0.I4zPop1KDT55QOE_QlEi-jh5TXg8nRjbnbDwq2VG1M8` text. Decoding it with base64 tell us that, it is jwt token with hs256 algorithm

![](base64.png)

After some research on jwt tokens and jwt token cracking. I found a tool https://github.com/ticarpi/jwt_tool. Using it we can break jwt token to get the secret key
so i used it with `rockyou.txt`.

![](jwt_tool.png)

FLAG : `cybergrabs{perrademierda}`

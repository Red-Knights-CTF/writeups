# Crypto Challenge

## BreakMe - 500

### Description: 
```I encrypted important information and lost my private key! Can you help me to recover the content of the file?```

### Given: 
```2 Files were given i) encrypted.txt ii) public.pem```

### Objective: 
```To decrypt the text provided in "encrypted.txt"```

### What to do: 
```We need a private key in order to decipher the text, we have public key in "public.pem"```

### Tools Required: 
    python Compiler(Editor/Interpreter) -- mandatory
    RsaCtfTool -- optional 
Link --> https://pypi.org/project/rsactftool

### Solution:

    Step: Extract certificate if any -- failure
    Step: Check for any RSA keys -- success
    Command: openssl rsa -noout -text -inform PEM -in public.pem -pubin
    Output: Found the modulus "n" and key for encryption "e"

    Step: Convert the "n" in decimal -- success
    Command: python -c 'print(int("00be5f670c7cdfcc0bd34112d3bd71229fd3e446e531bf3516036c1258336f6c51",16))'
    Output: 86108002918518428671680621078381724386896258624262971787023054651438740237393

    Step: Crack the cipher using RsaCtfTool
    Command: ./RsaCtfTool.py -n 86108002918518428671680621078381724386896258624262971787023054651438740237393 -e 65537 --uncipherfile encrypted.txt
    Output: HEX : 0x0002436131bce8ad1635e4fc004146464354467b5065726d5265636f72647d0a
		INT (big endian) : 3998731487633352107852441255033768239881091376738602013454220231226719498
		INT (little endian) : 4744677628729114467634823050067592469332131705762415234912324665256955806208
		STR : b'\x00\x02Ca1\xbc\xe8\xad\x165\xe4\xfc\x00AFFCTF{PermRecord}\n'

### Flag: 
    AFFCTF{PermRecord}

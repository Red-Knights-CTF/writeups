# Crypto Challenge

## Le SAGE doré - 

### Description: 
```We have to use SAGE language```

### Given: 
```A website containing encrypted_text and a public key```

### Objective: 
```To decrypt the "encrypted_text"```

### What to do: 
```Do some SAGE coding for decryption```

### Tools Required: 
    Nothing

### Solution:

    Step: Find p and q from public key -- success
    Website: factordb.com
    Output: p=1489304211816227 & q=5408427171993143
    
    Step: Decrypt using BlumGoldwasser function -- success
    Code: 
    bg = BlumGoldwasser();
    private = bg.private_key(p, q);
    flag= bg.decrypt(encrypted_flag, private);
    flag = "".join(str(m) for m in flatten(flag));
    flag
    Output: We get the flag
    
### Flag: 
    H2G2{0k_B0om3R}

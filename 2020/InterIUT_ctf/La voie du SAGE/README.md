# Crypto Challenge

## La voie du SAGE - 50 points

### Description: 
```We have to use SAGE language```

### Given: 
```A website containing ciphered_flag and ciphered_key```

### Objective: 
```To decrypt the "ciphered_flag"```

### What to do: 
```Do some SAGE coding for decryption```

### Tools Required: 
    Nothing

### Solution:
    
    Step: Decrypt using VigenereCryptosystem function -- success
    Code: 
    H = HexadecimalStrings()
    ciphered_flag = H("7f8e7e276140fead7d5b13a757d63a9a21599899479034")
    ciphered_key = H("375c37f5f6fdca46180cd0350e66c66ad228254a1446c7")
    vigenere = VigenereCryptosystem(H, len(ciphered_flag));
    flag = vigenere.deciphering(ciphered_key,ciphered_flag );
    flag
    Output: We get the flag
    
### Flag: 
    H2G2{S4ge_CrYpt0_1s_3Z}

### Author Name:
    Mann Pradhan {Ikshvaku}

# Crypto Challenge

## Le SAGE doré - 20 Points

### Description: 
```French -- Le vieux sage du village se rappelle avoir reçu un message chiffré il y a longtemps par l'un de ses disciples, mais a malheureusement depuis perdu la clé privé correspondante. Il a directement pensé à vous et pense que cet mission sera parfaite pour débuter votre ascension vers la voie du SAGE, retrouvez la clé privé ainsi que le contenu du message.```

```Translation in English -- The old sage of the village remembers having received an encrypted message a long time ago by one of his disciples, but has unfortunately since lost the corresponding private key. He has directly thought of you and thinks that this mission will be perfect to begin your ascent towards the path of the SAGE, find the private key as well as the content of the message.```

### Given: 
```A website containing encrypted_text and a public key```

Link --> https://sagecell.sagemath.org/?z=eJx1ks-KgzAQxu-C7xDYyy6IzJiY6GEP21K6h7IvIIuotRI2NuIflr79xtK1UVsYSPLj-2YyybyQ7efH4bD72u9c59TqmnRZVfpFe2l67TdDrmSR_pQXP1dDnVZaHX-zritbIutGtz3ZGLyf6IMUQy_VvziX57TXadYVUnrkuoxng13Hdcrz1VIe05PKKvJOXpMEPTIFmPj2SGKDcXNjYEtHBnMv3hjY0rsOnnpx6YXlXaaUT71TAcsLdmN3tqoB896sfDDr7dFbLWrg7M6rd1np5jUM5MBiBgHjYUSBi5gLJiIMOArOMKJvrmNGZpwX830RhEzElHIehiCQjgIa8wCQIuP4B_9DkhA=&lang=sage&interacts=eJyLjgUAARUAuQ==

### Objective: 
```To decrypt the "encrypted_text" using "pub_key"```

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

### Author Name:
    Mann Pradhan {Ikshvaku}

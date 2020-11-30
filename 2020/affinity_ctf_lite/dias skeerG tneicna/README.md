# Crypto Challenge

## dias skeerG tneicna - 20

### Description: 
```Nothing```

### Given: 
```1 File was given i) decode.me```

### Objective: 
```To decrypt the text provided in "decode.me"```

### What to do: 
```Decrypt the text using any cipher technique```

### Tools Required: 
    Text Editor

### Solution:
    
    Step: Check file format -- success
    Command: file decode.me
    Output: Just a regular text file with some cipher text
    Cipher Text: 554545532245{22434223_4223_42212322_55_234234313551_34553131423344}

    Step: Analyze the code manually  -- success
    Information: 1. Since the format of the string is like "...{...}...", one can easily guess the flag is there and substitution technique is used
                 2. Comparing cipher text with AFFCTF{...}
                 3. There is no 0 in the string, maybe 0 is not included
    Output: A = 55, F = 45, C = 53, T = 22

    Step: Make a table consisting of A-Z with there codes -- failure
    Output: A = 55
            B = 54
            C = 53
            D = 52
            E = 51
            F = 50 ...

    Step: Make a table consisting of A-Z with there codes without using 0 -- failure
    Output: A = 55
            B = 54
            C = 53
            D = 52
            E = 51
            F = 45 ...      

    Step: In previous step we get the code T = 21 and we cannot get code for Z, So make another table -- success
    Information: Playfair cipher uses 25 blocks for A-Z by combining I/J in a single block
    Output: A = 55
            B = 54
            I/J = 42
            Z = 11

    Step: Crack the cipher simply putting the values
    Output: AFFCTF{THIS_IS_JUST_A_SIMPLE_MAPPING}

### Flag: 
    AFFCTF{THIS_IS_JUST_A_SIMPLE_MAPPING}

### Author Name:
    Mann Pradhan {Ikshvaku}

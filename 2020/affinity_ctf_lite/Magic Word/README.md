# Magic Word

**Category**: Reverse Engineering \
**Points**: 120

## Discription

We need a magic word to get the response here, can you discover it?

## Challenge

- Given magicword binary
- Print flag

## Solution

We were given a binary file:
1. [magicword](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Magic%20Word/magicword)

Running binary we were asked to enter a input

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Magic%20Word/magicword.png)

It was a simple binary that compare two strings. So we need to print out the right string(flag)

You can use any any debbuger you like. For this challenge i have used ```edb``` .
Stepover all the instructions until ```Incorrect Input``` is printed on the screen

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Magic%20Word/jmp.png)

Stepover one instruction and now we are on a ```jmp``` instrction that will take us to the end of the binary, but we want to print the flag on our screen.
So we will fill the jmp instruction with ```nop``` 

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Magic%20Word/nops.png)

Gradually stepover the instructions and you will get the flag printed on your screen

![](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Magic%20Word/flag_printed.png)

FLAG - AFFCTF{h4v3AG00dD4y}

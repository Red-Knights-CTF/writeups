# Fibonacci

**Category**: Forensics
**Points**: 200

Opening this file in a hex editor:
```
$ xxd Fibonacci.7z | less
00000000: 4242 4242 3742 7abc 42af 271c 0042 04c9  BBBB7Bz.B.'..B..
00000010: 336d e569 0542 0000 0000 0000 5a00 0000  3m.i.B......Z...
00000020: 0000 4200 0077 9ed7 14e0 0be2 0561 5d00  ..B..w.......a].
00000030: 2168 b490 09c2 6442 c064 0461 7378 6c59  !h....dB.d.asxlY
00000040: 041b 7ec3 e075 08cf 3b81 a186 1f0c 2557  ..~..u..;.....%W
00000050: fded 72e7 04b6 20eb a242 dcc7 e2f1 ee76  ..r... ..B.....v
00000060: 407f 6fa8 09dc e8db 19d4 ea35 0743 14a5  @.o........5.C..
```

We can almost see the `7zip` header, but it seems to be crowded with `B`
characters.

Looking closely, we see that there are `B` characters at these positions:
```
0 1 1 2 3 5 8 13 21 ...
```

This is the fibonacci sequence, so let's just remove these characters and see
what happens.

```python
def gen_fib(n):
    ans = [0, 1]
    while ans[-1] < n:
        ans.append(ans[-1] + ans[-2])
    return ans


i = 0
with open('out.7z', 'wb') as fout:
    with open('Fibonacci.7z', 'rb') as fin:
        fibs = gen_fib(1000)
        print(fibs)
        fibs = set(fibs)
        print(fibs)

        while True:
            b = fin.read(1)
            if b == b'':
                break

            if i not in fibs:
                fout.write(b)

            i += 1
```

Then we can just unzip:
```
$ 7z e out.7z
$ cat Fibonacci | grep AFFCTF
"AFFCTF{Hitchhiker}," said Deep Thought, with infinite majesty and calm.”
```

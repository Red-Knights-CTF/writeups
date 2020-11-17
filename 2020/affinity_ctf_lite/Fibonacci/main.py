def gen_fib(n):
    ans = [0, 1]
    while ans[-1] < n:
        ans.append(ans[-1] + ans[-2])
    return ans


i = 0
with open('out.7z', 'wb') as fout:
    with open('Fibonacci.7z', 'rb') as fin:
        fibs = gen_fib(1000)
        fibs = set(fibs)
        print(fibs)

        while True:
            b = fin.read(1)
            if b == b'':
                break

            if i not in fibs:
                fout.write(b)

            i += 1

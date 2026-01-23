def fib_memo(n, mem={}):
    if n in mem:
        return mem[n]
    if n <=1:
        mem[n] = n
    else:
        mem[n] = fib_memo(n-1, mem) + fib_memo(n-2, mem)
    return mem[n]

print(fib_memo(7))
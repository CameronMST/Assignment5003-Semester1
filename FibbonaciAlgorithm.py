def fib_memo(n, mem={}):
    if n in mem:
        return mem[n]
    if n <=1:
        mem[n] = n
    else:
        mem[n] = fib_memo(n-1, mem) + fib_memo(n-2, mem)
    return mem[n]

print(fib_memo(7))
#(CodeLucky, 2025)





#-------------------------------
#References

#CodeLucky (2025). Fibonacci Sequence: Classic Dynamic Programming Example with Python - CodeLucky. [online] CodeLucky. Available at: https://codelucky.com/fibonacci-sequence/ [Accessed 23 Jan. 2026].
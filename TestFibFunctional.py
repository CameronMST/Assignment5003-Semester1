def fib_memo(n, mem={}):
    if n in mem:
        return mem[n]
    if n <=1:
        mem[n] = n
    else:
        mem[n] = fib_memo(n-1, mem) + fib_memo(n-2, mem)
    return mem[n]

assert(fib_memo(2)) == 1
assert(fib_memo(3)) == 2
assert(fib_memo(4)) == 3
assert(fib_memo(5)) == 5
assert(fib_memo(6)) == 8
assert(fib_memo(7)) == 13
assert(fib_memo(8)) == 21
assert(fib_memo(9)) == 34
assert(fib_memo(10)) == 55
#(CodeLucky, 2025)





#-------------------------------
#References

#CodeLucky (2025). Fibonacci Sequence: Classic Dynamic Programming Example with Python - CodeLucky. [online] CodeLucky. Available at: https://codelucky.com/fibonacci-sequence/ [Accessed 23 Jan. 2026].
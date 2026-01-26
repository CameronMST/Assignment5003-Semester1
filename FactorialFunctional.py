#number = None
def factorial(number):
    return 1 if number <= 1 else number * factorial(number-1) #(GeeksforGeeks, 2014)

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(9) == 362880
assert factorial(10) == 3628800

#References -----------------------------------------------

#GeeksforGeeks (2014). Factorial of a Number. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/dsa/program-for-factorial-of-a-number/. [Accessed 23/01/2026].
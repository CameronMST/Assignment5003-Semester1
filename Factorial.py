number = int(input("Enter a number to factorial: "))

def factorial(number):
    return 1 if number <= 1 else number * factorial(number-1)

print(factorial(number)) #(GeeksforGeeks, 2014)


#References -----------------------------------------------

#GeeksforGeeks (2014). Factorial of a Number. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/dsa/program-for-factorial-of-a-number/. [Accessed 23/01/2026].
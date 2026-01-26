import tracemalloc
import time

number = 5
def factorial(number):
    time.start_time = time.time()
    tracemalloc.start()

    return 1 if number <= 1 else number * factorial(number-1)
print(factorial(number)) #(GeeksforGeeks, 2014)

current, peak = tracemalloc.get_traced_memory()
print(f"\n--- Execution Time: {(time.time() - time.start_time) * 1000:.3f} miliseconds ---")
print(f"--- Memory Usage: {peak:.2f} bytes ---")

#References -----------------------------------------------

#GeeksforGeeks (2014). Factorial of a Number. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/dsa/program-for-factorial-of-a-number/. [Accessed 23/01/2026].
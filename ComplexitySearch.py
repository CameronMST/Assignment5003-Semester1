import tracemalloc
import time

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6] #Has to be sorted, because median and IQR are statistics of order.


#In the GUI Implementation there is a sorting Algorithm before this function, although we want the complexity of the search not the sort.
#As we already know the sort comlexity

def Statistical_Search(my_list):
    
    time.start_time = time.time()
    tracemalloc.start()

    #Smallest & Largest
    smallest = my_list[0]
    largest = my_list[-1]

    #Median
    if len(my_list) % 2 == 1:
        median = my_list[len(my_list)//2]
    else:
        median = (my_list[len(my_list)//2 - 1] + my_list[len(my_list)//2]) / 2.
    
    #Inter Quartile
    n = len(my_list)
    LowerIQF = my_list[n // 4]
    UpperIQF = my_list[(3 * n) // 4]

    #Mode
    max_count = 0
    modes = []
    for item in my_list:
        count = my_list.count(item)
        if count > max_count:
            max_count = count
            modes = [item]
        elif count == max_count and item not in modes:
            modes.append(item) #(GeeksforGeeks, 2018)

    return smallest, largest, median, LowerIQF, UpperIQF, modes

results = Statistical_Search(my_list)
print(f'\nSmallest: {results[0]}\nLargest: {results[1]}\nMedian: {results[2]}\nLower IQF: {results[3]}\nUpper IQF: {results[4]}\nMode: {results[5]} \n')

current, peak = tracemalloc.get_traced_memory()
print(f"\n--- Execution Time: {(time.time() - time.start_time) * 1000:.3f} miliseconds ---")
print(f"--- Memory Usage: {peak:.2f} bytes ---")

#References

#GeeksforGeeks (2018). Finding Mean, Median, Mode in Python without libraries. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/finding-mean-median-mode-in-python-without-libraries/.

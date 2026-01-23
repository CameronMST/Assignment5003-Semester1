def bubblesort(my_list):
    for iter in range(len(my_list)-1):
            for i in range(len(my_list)-iter-1):
                if my_list[i] > my_list[i+1]:
                    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list
                
print(bubblesort([34, 25, 26, 33]))
#(GeeksforGeeks, 2014)




#References ----------------------------------------------
#GeeksforGeeks (2014). Bubble Sort Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/.[Accessed 23/01/2026]
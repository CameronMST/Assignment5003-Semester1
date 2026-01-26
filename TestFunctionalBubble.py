
my_list = [5, 22, 9, 55, 22]
equality = '-'

def bubblesort(my_list):

    for iter in range(len(my_list)-1):
            for i in range(len(my_list)-iter-1):

                if equality == '-':
                    if my_list[i] < my_list[i+1]:
                        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                #Descending - Placed at top for default Ascending if any other option is entered
                else:
                    if my_list[i] > my_list[i+1]:
                        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                #Ascending
    return my_list

if equality == '+':
    assert(bubblesort(my_list)) == [5, 9, 22, 22, 55]
else:
    assert(bubblesort(my_list)) == [55, 22, 22, 9, 5]




#(GeeksforGeeks, 2014)




#References ----------------------------------------------
#GeeksforGeeks (2014). Bubble Sort Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/.[Accessed 23/01/2026]
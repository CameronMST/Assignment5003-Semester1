my_list = [5, 22, 9, 55, 22]
equality = '-'

def selection_sort(my_list):
    for iter in range(0, len(my_list)-1):
        min = iter
        for i in range(iter + 1, len(my_list)):
            
            if equality == '-':
                if my_list[i] > my_list[min]:
                    min = i
            #Descending - Placed at top for default Ascending, if anyother option is entered.
            else:
                if my_list[i] < my_list[min]:
                    min = i
            #Descending
        my_list[iter], my_list[min] = my_list[min], my_list[iter]
    return my_list

selection_sort(my_list) # (W3Schools, n.d)
if equality == '+':
    assert(selection_sort(my_list)) == [5, 9, 22, 22, 55]
else:
    assert(selection_sort(my_list)) == [55, 22, 22, 9, 5]


#Reference
#W3schools, (n.d.). DSA Selection Sort. [online] Available at: https://www.w3schools.com/dsa/dsa_algo_selectionsort.php.[Accessed 23/01/2026].
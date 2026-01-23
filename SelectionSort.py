equality = input("Enter \'+\' For Ascending or \'-\' For Descending: ")
my_list = [64, 21, 22, 19, 5, 5]

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

print(selection_sort(my_list)) # (W3Schools, n.d)

#Reference
#W3schools, (n.d.). DSA Selection Sort. [online] Available at: https://www.w3schools.com/dsa/dsa_algo_selectionsort.php.[Accessed 23/01/2026].
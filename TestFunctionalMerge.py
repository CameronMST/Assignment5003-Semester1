
my_list = [5, 22, 9, 55, 22]
equality = '-'

def Merge_Sort(my_list):

    
    if len(my_list) > 1:
        mid = len(my_list) // 2
    
        
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        Merge_Sort(left_half)
        Merge_Sort(right_half)

        left_index, right_index, main_index = 0, 0, 0

        while left_index < len(left_half) and right_index < len(right_half):
            
            #Descending Order
            if equality == '-':
                if left_half[left_index] > right_half[right_index]:
                    my_list[main_index] = left_half[left_index]
                    left_index += 1
                    main_index += 1
            
                else:
                    my_list[main_index] = right_half[right_index]
                    right_index += 1
                    main_index += 1
            #Ascending Order, Placed Below for Defaulting.
            else:
                if left_half[left_index] < right_half[right_index]:
                    my_list[main_index] = left_half[left_index]
                    left_index += 1
                    main_index += 1

                else:
                    my_list[main_index] = right_half[right_index]
                    right_index += 1
                    main_index += 1    

        while left_index < len(left_half):
            my_list[main_index] = left_half[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_half):
            my_list[main_index] = right_half[right_index]
            right_index += 1
            main_index += 1 #(Tutorialspoint, 2019)

    return my_list
Merge_Sort(my_list)

if equality == '+':
    assert(Merge_Sort(my_list)) == [5, 9, 22, 22, 55]
else:
    assert(Merge_Sort(my_list)) == [55, 22, 22, 9, 5]

#References

#Tutorialspoint, (2019). Data Structures - Merge Sort Algorithm - Tutorialspoint. [online] Available at: https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm.
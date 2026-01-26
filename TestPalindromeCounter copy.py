def countPS(InputString):
    string_length = len(InputString)
    
    memo = [[-1 for i in range(string_length)] for i in range(string_length)]

    count = 0
    for i in range(string_length):
        for j in range(i + 1, string_length):
            
            if isPalindrome(i, j, InputString, memo) == True:
                count += 1
    return count


def isPalindrome(left_index, right_index, InputString, memo):                            
    if left_index == right_index:
        return True
    
    if right_index == left_index + 1 and InputString[left_index] == InputString[right_index]:
        return True
    
    if memo[left_index][right_index] != -1:
        return memo[left_index][right_index]
    
    if InputString[left_index] == InputString[right_index] and isPalindrome(left_index + 1, right_index - 1, InputString, memo) == True:
        memo[left_index][right_index] = True
    else:
        memo[left_index][right_index] = False
    
    return memo[left_index][right_index]


print("Total palindromic substrings are:", countPS("Hello"))




#Appendicies
#Single Letters are debated whether they're palindromic, as this is a substring problem we will not count them.

#References
#GeeksforGeeks (2016). Palindrome Substrings Count. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/dsa/count-palindrome-sub-strings-string/. [Accessed 24 Jan. 2026].

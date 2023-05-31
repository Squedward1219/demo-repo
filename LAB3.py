# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given
# You might add a helper functions as long as it is recursive and named helper_<function name as given in this file>



def replace(numList, old, new): 
    """
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    """
    ## YOUR CODE STARTS HERE

    #if numList is empty, return an empty list
    if not numList:
        return []
    #if the first element of numList matches old, replace it with new and call replace on the rest of the list
    elif numList[0] == old:
        return [new] + replace(numList[1:], old, new)
    else:
    #if the first element of numList does not match old, keep it and call replace on the rest of the list
        return [numList[0]] + replace(numList[1:], old, new)
    pass

def serial_star(n):
    """
        >>> serial_star(0)
        '*'
        >>> serial_star(3)
        '********'
        >>> serial_star(4)
        '****************'
    """
    ## YOUR CODE STARTS HERE
    if n == 0:
        return '*'
    elif n > 0:

        #make sure n isn't a float
        if isinstance(n, int) == True:
            return '*' + serial_star(2**n)
        elif isinstance(n, int) == False:
            return "Can't return a root of a an asterisk"

    #make sure n isn't negative
    elif n < 0:
        return "Can't return a fraction of an asterisk"
    pass

def get_match(num1, num2):
    """
        >>> get_match(6598, 509)
        1
        >>> get_match(654886625, 115568)
        0
        >>> get_match(654886625, 12880605)
        4
    """
    ## YOUR CODE STARTS HERE
    #one of the numbers is 0, so there are no matching digits
    if num1 == 0 or num2 == 0:
        return 0
    #if the last digits of num1 and num2 match, 
    #increase the count by 1 and recursively check the rest of the digits
    elif num1 % 10 == num2 % 10:
        return 1 + get_match(num1 // 10, num2 // 10)
    #if the last digits of num1 and num2 do not match, 
    #simply check the rest of the digits
    else:
        return get_match(num1 // 10, num2 // 10)

    pass


def neighbor(num):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    ## YOUR CODE STARTS HERE

    #single-digit number is returned as is
    if num < 10:
        return num

    last_digit = num % 10
    num //= 10

    # recursive call for the rest of the number
    previous_number = neighbor(num)  

    #current digit is a duplicate, so discard it
    if previous_number % 10 == last_digit:
        return previous_number   

    ##current digit is different, add it to the result
    else:
        return previous_number * 10 + last_digit  

    pass




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(neighbor, globals(), name='LAB3',verbose=True)

if __name__ == "__main__":
    run_tests()




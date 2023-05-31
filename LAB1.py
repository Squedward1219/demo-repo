# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def intersection(d1, d2):
    """
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':5, 'a':5, 'b':9, 'c':12}) 
        {'a': 5, 'd': 5}
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':8, 'a':51, 'b':9, 'c':12}) 
        {}
        >>> dict_one = {'a':5, 'b':7, 'd':5, 'c':'32', 'art':35.6}
        >>> dict_two = {'d':8, 'a':51, 'b':9, 'c':'32'}
        >>> intersection(dict_one, dict_two) 
        {'c': '32'}
        >>> dict_one
        {'a': 5, 'b': 7, 'd': 5, 'c': '32', 'art': 35.6}
        >>> dict_two
        {'d': 8, 'a': 51, 'b': 9, 'c': '32'}
    """
    # - YOUR CODE STARTS HERE -

    #empty dictionary for matching terms
    twins = {}
    #cylce through the first dictionary
    for term in d1:

        #find terms that have same input first and then verify the output is the same
        if term in d2 and d1[term] == d2[term]:

            #add to new dict for matching terms
            twins[term] = d1[term]
            
    return twins        

    pass


def frequency(d):
    """
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'e': 5, 'f': 1}) 
        1
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1})                 
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6})   
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6, 'ret': 6, 'z': 5}) 
        6
    """
    # - YOUR CODE STARTS HERE -

    #Create an empty dictionary to list the frequencies of each value
    frequency = {}

        #assign the value to the dictionary with a value of 1 and if it repeats increase the value for that entry 
    for value in d.values():

        if value not in frequency:
                frequency[value] = 1

        else:
                frequency[value] += 1
        #Cycle through the values to determine the value with the highest frequency
    highest_value = None
    highest_count = 0
    for value, count in frequency.items():
        if count > highest_count:
            highest_count = count
            highest_value = value
    return highest_value

    pass



def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3, 'un':1})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -

    #empty dictionary
    inverted_d = {}
    #dictionary to keep track of frequencies
    value_count = {}
    
    for key, value in d.items():
        #add the values that aren't in the inverted dictionary
        if value not in value_count:
            value_count[value] = 1
            inverted_d[value] = key
        else:
            #remove value if it gets repeated
            value_count[value] += 1
            if value_count[value] == 2:
                inverted_d.pop(value, None)
    return inverted_d
    pass



def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(intersection, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()


# Recitation Activity #12

def hailstone(n):
    '''
        >>> my_gen = hailstone(6) 
        >>> [item for item in my_gen]
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
        >>> my_gen = hailstone(5) 
        >>> next(my_gen) 
        5
        >>> next(my_gen)
        16
        >>> next(my_gen)
        8
        >>> next(my_gen)
        4
        >>> next(my_gen)
        2
        >>> next(my_gen)
        1
        >>> next(my_gen)
        Traceback (most recent call last):
        StopIteration
    '''
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    yield n

    
    pass
def run_tests():
    import doctest

    #Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    #doctest.run_docstring_examples(addToTrie, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()





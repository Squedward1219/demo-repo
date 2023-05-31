# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    import math
    end = math.sqrt(area)
    end = round(end) + 1
    factors = list(range(1,end))
     
    for l in factors:
        w = area // l
        #Make sure side lengths are positive 
            
        #Hypothetical area and perimeter 
        tempArea = (l * w)
        tempPer = 2*(l+w)
            
        #Eliminate negative side lengths
        
        if w < 0 or l < 0:
            return False
        else:

            #Cycle through 

            if tempArea == area and tempPer == perimeter:

                #Compare the side lengths
            
                if l > w:
                    return l

                elif w > l:
                    return w
                #If you can't find a match and you're at the last term, return False     
            elif l == factors[(len(factors)-1)]:
                return False

    pass




def get_index(num, digit):
    """
        >>> get_index(1495, 5)
        1
        >>> get_index(1495, 1)
        4
        >>> get_index(1495423, 4)
        3
        >>> get_index(1495, 7)
        -1
    """
    #- YOUR CODE STARTS HERE
    #counter variable for the position
    position = 1

    #to make sure the digit is in the number 
    while num > 0:
        #check the digit in the ones place
        if num % 10 == digit:
            
            return position
        #divide by ten and discard the digit in the ones place
        num = num // 10
        #increase counter variable for the position
        position += 1
    #output if digit can't be found in the number
    return -1

    pass



def unique_largest(num):
    """
        >>> unique_largest(123132)
        False
        >>> unique_largest(7264578364)
        True
        >>> unique_largest(2)
        True
        >>> unique_largest(444444)
        False
    """
    #- YOUR CODE STARTS HERE
    greatestnum = 0
    
    while num > 0:

        digit = num % 10

        if digit > greatestnum:

            greatestnum = digit
            
        elif digit == greatestnum:

            greatestnum = 0
    if greatestnum > 0:
        return True
    if greatestnum == 0:
        return False
            
            
        
        
    pass



def joined_list(n):
    """
        >>> joined_list(5) 
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joined_list(-8) 
        [-8, -7, -6, -5, -4, -3, -2, -1, -1, -2, -3, -4, -5, -6, -7, -8]
    """
    #- YOUR CODE STARTS HERE
    #list counting from 1 to the number if it's positive
    if n > 0:
        l1 = list(range(1,n+1))

    #list counting from the number to -1 if it's negative    
    elif n < 0:
        l1 = list(range(n,0))
    #make a second list com
    l2 = [] + l1
    l2.reverse()
    both = l1 + l2
    return both
    pass



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    pass
    seq = []
    while num != 1:
        seq.append(num)
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = 3 * num + 1
    seq.append(num)
    return seq
            
        



def is_isomorphic(word1, word2):
    """
        >>> is_isomorphic("egg", "add")
        True
        >>> is_isomorphic ("foo", "car") 
        False
        >>> is_isomorphic ("badc", "baba") 
        False
    """
    #- YOUR CODE STARTS HERE
    mapping = {}
    for i in range(len(word1)):
        if word1[i] not in mapping:
            if word2[i] in mapping.values():
                return False
            mapping[word1[i]] = word2[i]
        elif mapping[word1[i]] != word2[i]:
            return False
    return True
 
    pass




def translate(translation_file, msg):
    """
        >>> translate('abbreviations.txt', 'c u in 5.')
        'see you in 5.'
        >>> translate('abbreviations.txt', 'gr8, cu')
        'great, see you'
        >>> translate('abbreviations.txt', 'b4 lunch, luv u!')
        'before lunch, love you!'
    """
    # Open file and read lines into one string all the way to the end of the file
    with open(translation_file) as file:   
        contents = file.read()

    #- YOUR CODE STARTS HERE
    # Create a dictionary to store the translations from the .txt file
    translations = {}
    for line in file:
        abbrev, real = line.strip().split(":")
        translations[abbrev] = real
            
    # Split the message into words and translate each word
    translated_words = []
    for word in msg.split():
        if word in translations:
            translated_words.append(translations[word])
        else:
            translated_words.append(word)
            
    # Join the translated words to create the final translated string
    return " ".join(translated_words)
    pass




def addToTrie(trie, word):
    """      
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS
    #set up an dictionary for the node traversing
    current_node = trie
    #make sure each letter is in the dictionary and add it if it isn't, but with no coordinating value
    for letter in word:
        if letter not in current_node:
            current_node[letter] = {}
        current_node = current_node[letter]
    #If the node completes a word then the entry for that dictionary should be word:true
    current_node["word"] = True

    pass







def run_tests():
    import doctest

    #Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(hailstone, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()




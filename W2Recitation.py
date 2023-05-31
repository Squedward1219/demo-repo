# Recitation Activity 1

def translate(translation, msg):
    """
        translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """     
    # -- YOUR CODE STARTS HERE

    msg = msg.lower()
    phrases = msg.split(' ')
    temp = []
    for word in phrases:
        if word in translation:
            temp.append(translation[word])
        else:
            temp.append(word)
    temp = ' '.join(temp)
    msg = temp
    return msg



    pass






'''
ferd = translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
print(ferd)
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()

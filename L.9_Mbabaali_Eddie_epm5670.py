'''
Full Name: Eddie Mbabaali
Team Members: Eddie Mbabaali
ID: 928391864
Date: 10/14
Filename: L.9_Mbabaali_Eddie_epm5670
Purpose: checking errors
'''

'''
1. Type error is when you try to divide a string by an int
'''
def err1a(var,wrd):
    print(var/wrd)

def err1b(var1,var2):
    print(var/var2)


'''
2. Type Value Error is when the function receives a wrong value
'''
def err2a(sq1):
    print(sq1**2)

def err2b(sq2):
    print(sq2**2)


'''
3. Name Error is when there's a mispelling
'''
def err3a():
    abc = 100
    print(acb)
def err3b():
    a = 1000
    print(a)


'''
4. Index Error is when the index can't access a value in the list b/c it's out of range
'''
def err4a(lst):
    for i in range(lst):
        print(lst[8])
def err4b(lst):
    for i in range(lst):
        print(lst[27])



def main():
    word = "class"
    num = 7
    err1a(word,num)

    x = "tutor"
    y = 7
    err1b(x,y)

    n = "class"
    v = "tutor"
    err2a(n)
    err2b(v)


    err3a()
    err3b()


    lst1 = [1,2,3]
    lst2 = [3,4,5,6]
    err4a(lst1)
    err4b(lst2)

main()

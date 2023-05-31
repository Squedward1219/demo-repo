'''
Full Name: Eddie Mbabaali
ID: 928391864
Date: 9/09/2022
Filename: L3_Mbabaali_Eddie_epm5670.py
Purpose: Functions that use lists as parameters
'''

def avg_num(numbers):
    total = 0
    group = 0
    for number in numbers:
        total = total + number
        group += 1
    avg = total / group
    print(str(avg))
    

def sum_num(numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(str(total))
    









list1 = [1,3,5,7,9,7]
avg_num(list1)
sum_num(list1)
list2 = [11,31,51,71,90]
avg_num(list2)
sum_num(list2)

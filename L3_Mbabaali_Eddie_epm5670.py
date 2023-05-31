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


def exp_growth(numbers):
    k=.05
    t=10
    e=2.7
    for number in numbers:
        A = number
        P = A * (e ** (k * t))
        print(str(P))


def point_distance(x):
    for i in x:
        diffx = x[0] - x[2]
        diffy = x[1] - x[3]
        m = ((diffx ** 2) + (diffy ** 2))
        dist = m ** 0.5
    print(str(dist))

list1 = [1,3,5,7,9,7]
avg_num(list1)
sum_num(list1)
list2 = [11,31,51,71,90]
avg_num(list2)
sum_num(list2)
A = [10,1400,1000,200]
exp_growth(A)
list1 = [2,-4,3,3]
point_distance(list1)
list2 = [4,5,7,2]
point_distance(list2)

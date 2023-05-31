'''
Full Name: Eddie Mbabaali
ID: epm5670
Date: 9/23/2022
Filename:L.5_Mbabaali_Eddie_epm5670.py
Purpose:Sort numbers in ascending and descending order
'''

#Problem 1
def ascender(group):
    group.sort()
    print(group)

    
def descender(group):
    group.sort()
    group.reverse()
    print(group)

    
def main() :
    nums = [ 1, 10, 3, 15, 6, 8 ] 
    ascender(nums)
    descender(nums)

main()

'''
Full Name: Eddie Mbabaali
ID: epm5670
Date: 9/30/2022
Filename:A.1_Mbabaali_Eddie_epm5670.py
Purpose: Manipulate lists
'''

#Problem 1

def popular(group, n):
    maxcount = 0;
    element_having_max_freq = 0;
#Comparing Numbers
    for i in range(0, n):
        count = 0
        for j in range(0, n):
#Increasing Count for the most popular number
            if(group[i] == group[j]):
                count += 1
            if(count > maxcount):
                maxcount = count
            mostFrequent = group[i]
    print(str(mostFrequent) + ", " + str(count))

#Problem 2
def maximum(group, start, end):
    biggest = group[start]
    for i in range(start,end):
        if(group[i] > biggest):
            biggest = group[i]
    return biggest
def windowSlide(group, windSize):
    newWind = []
    end = windSize - 1
    for i in range(len(group)-end):
                    x = maximum(group, i, i + windSize)
                    newWind = newWind + [x]
    return newWind        

# Driver Code
def main():
#P1
    nums = [40,50,30,40,50,30,30]
    n = len(nums)
    popular(nums, n)
#P2
    l1 = [2, 5, 12, 3, 4]
    l2 = [1, 3, 5, 1, 2, 4, 7, 8]
    l3 = [1, 3, 0, 3, 5, 3, 6, 2, 8]
    windowSlide(l1, 2)
    windowSlide(l2, 4)
    windowSlide(l3, 3)

main()

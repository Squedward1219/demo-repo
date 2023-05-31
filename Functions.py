'''
Full Name: Eddie Mbabaali
ID: 928391864
Date: 8/28/2022
Filename: Functions
Purpose: Utilize mathematical operators via python
'''

def exp_growth(A,k,t):

    # start your code below this line -- make more lines if needed

    #combine the exponents
    i = k * t;

    #define e
    e = 2.7;

    #compute the inputs
    P = A * (e ** i);

    # finish your code above this line

    return P

def point_distance(x1,y1,x2,y2):

    # start your code below this line -- make more lines if needed

    #horizontal distance
    diffx = x2 - x1;

    #vertical distance
    diffy = y2 - y1;
    
    #distance between both points
    m = ((diffx ** 2) + (diffy ** 2));

    d= m**0.5
    # finish your code above this line

    return d

def slope(x1,y1,x2,y2):

    # start your code below this line -- make more lines if needed

    #horizontal distance
    diffx = x2-x1;

    #vertical distance
    diffy = y2-y1;
    
    #slope between both points
    m = diffy / diffx;
    
    # finish your code above this line

    return m

def main():

    p1=exp_growth(10000,.05,10)
    print("p1: ", p1) 

    p2=exp_growth(140000,.07,25)
    print("p2: ", p2)
    
    d1=point_distance(2,3,-4,3)
    print("d1: ", d1)

    d2=point_distance(4,7,5,2)
    print("d2: ", d2)

    m1=slope(2,3,-4,3)
    print("m1: ", m1)

    m2=slope(4,7,5,2)
    print("m2: ", m2)

main()

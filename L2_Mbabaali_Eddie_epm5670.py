'''
Full Name: Eddie Mbabaali
ID: 928391864
Date: 9/02/2022
Filename: L2_Mbabaali_Eddie_epm5670.py
Purpose: Utilize functions via python
'''
def avg_num (x,y) :

    avg = ((x +y) /2);

    return avg


def print_str(string) :

    print(str(string));

def my_num():

    number = int(input("Enter a  number: "));

    print(number);


def hello_msg() :

    print("Hello World");

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

    print(m);
#Problem 1
avg = avg_num(34,58);
print_str(avg);
print_str("I love Computer Science");
my_num();
hello_msg();

#Problem 2
p21 = exp_growth(10000, .05, 10);
print_str(p21);

p22 = exp_growth(140000, .07, 25);
print_str(p22);

#Problem 3
p31 = point_distance(2,3,-4,3);
print_str(p31);

p32 = point_distance(4,7,5,2);
print_str(p32);

#Problem 4
p41 = slope(2,3,-4,3);
print_str(p41);

p42 = slope(4,7,5,2);
print_str(p42);


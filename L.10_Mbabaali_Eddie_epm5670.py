'''
Full Name: Eddie Mbabaali
ID:928391864
Date: 10/21/22
Filename: L.10_Mbabaali_Eddie_epm5670.py
Purpose: to become comfortable with the constructs we have learned so far
including function, iterations, conditionals, lists, and files and identify any
gaps in your learning and the concept.
'''


def create_file(fn):
    fn = open("fn.txt", 'w')
    fn.close()



def read_file(fn):
    infile = open("fn.txt", 'r')
    info = infile.read()
    infile.close()
    print(info)


    


def read_file_lines(fn):
    data = []
    infile = open("fn.txt", 'r')
    for line in infile:
        data = data + [line]
    infile.close()
    print(data)

    



def write_to_file(fn, lst):
    infile = open("fn.txt", 'w')
    if list == []:
        print("List is empty")
    else:
        for text in lst:
            fn.write(text)

        
    

def append_to_file(fn, lst):
    infile = open("fn.txt", 'w')
    for text in lst:
        fn.write(text)
            
    
    
    

def main():
    fn = "newfile"
    create_file(fn)
    read_file(fn)


    
main()

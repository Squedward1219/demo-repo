'''
Full Name: Eddie Mbabaali
Team Members: Joohan Son, Andrew Xu, Aseem B, Eddie M
ID:
Date:11/18/22
Filename:P1_Mbabaali_Eddie_epm5670.py
Purpose:The purpose of the project is to implement all the concepts you 
have learned in this course. This project would require you to
implement a word-information-table.
'''



def read_analyze(fname):
    infile=open(fname,"r")
    

    line=infile.read()
    lst=line.split()
    infile.close()
    #print(lst)
    num=len(lst)


    reference=open(fname,"r")
    line1a=reference.readline()
    line1b=line1a.split()
    line1len=len(line1b)
    reference.close()

    
    #print(line1len)
    setlst=[]
    lst2=[]
    lst3=[]
    lst4=[]
    lst5=[]
    lst6=[]

    for i in range(len(lst)):
        counter=0
        for j in range(0,i):
            counter=counter+0
            if(lst[i]==lst[j]):
                counter=counter+1
            else:
                counter=counter+0
        if(counter==0):
            setlst=setlst+[lst[i]]
    #print(setlst)
    
    for i in range(len(setlst)):
        counter=0
        for j in range(len(lst)):
            if(lst[j]==setlst[i]):
                counter=counter+1
        lst2=lst2+[counter]

    #print(lst2)

    for i in range(len(setlst)):
        if(i<line1len):
            lst3=lst3+[1]
        else:
            lst3=lst3+[2]
    #print(lst3)

    
    for i in range(len(setlst)):
        if(i<line1len and setlst[i]==lst[i]):
            lst4=lst4+[i+1]
        elif(i>=line1len and setlst[i]==lst[i]):
            lst4=lst4+[i-(line1len-1)]
        elif(i<line1len and setlst[i]==lst[i+1]):
            lst4=lst4+[i+2]
        elif(i>=line1len and setlst[i]==lst[i+1]):
            lst4=lst4+[i-(line1len-2)]
    #print(lst4)

    lst5=[0 for i in range(len(setlst))]
    for i in range(len(setlst)):
        if(lst2[i]!=1):
            counter=0
            for j in range(len(lst)):
                if(setlst[i]==lst[j]):
                    counter=j
                    if(counter>=line1len):
                        lst5[i]=2
                    else:
                        lst5[i]=1
    #print(lst5)

    lst6=[0 for i in range(len(setlst))]
    for i in range(len(setlst)):
        if(lst2[i]!=1):
            counter=0
            for j in range(len(lst)):
                if(setlst[i]==lst[j]):
                    counter=j
                    if(counter>=line1len):
                        lst6[i]=j-(line1len-1)
                    else:
                        lst6[i]=i+1
    #print(lst6)
    
    
    table(setlst,lst2,lst3,lst4,lst5,lst6)

def freq(lst,element):
    counter=0
    for i in lst:
        if i==element:
            counter=counter+1
    return counter

def table(lst,lst2,lst3,lst4,lst5,lst6):
    row=len(lst)+1
    column=6
    
    table=[[0 for i in range(column)]for j in range(row)]
    table[0][0]='Words'
    table[0][1]="Occurrences"
    table[0][2]="Line"
    table[0][3]="Word #"
    table[0][4]="Line"
    table[0][5]="Word #"
    
    for i in range(row-1):
        table[i+1][0]=lst[i]

    for i in range(row-1):
        table[i+1][1]=lst2[i]

    for i in range(row-1):
        table[i+1][2]=lst3[i]

    for i in range(row-1):
        table[i+1][3]=lst4[i]
    
    for i in range(row-1):
        table[i+1][4]=lst5[i]

    for i in range(row-1):
        table[i+1][5]=lst6[i]
    
    
    for row in table:
        print(row)

def main():
    read_analyze("p1.txt")
    

main()




______________


def update_word_table(word_table, new_word, line_count, word_index):
    found = False
    for lst in word_table:
        if new_word == lst[0]:
            lst[1]+=1
            lst += [line_count, word_index]
            found = True
    if found == False:
        word_table += [[new_word, 1, line_count, word_index]]
    return word_table

def process_words(word_table, words, line_count):
    word_index = 0
    for w in words:
        word_index += 1
        word_table = update_word_table(word_table, w, line_count, word_index)

def word_processor(file_name):
    fh = open(file_name, "r")
    line = fh.readline()
   
    line_count = 0
    word_table = []
    
    while line:
        line_count += 1
        words = line.split()
        process_words(word_table, words, line_count)
        line = fh.readline()
    
    fh.close()
    return word_table

def print_row(row):
    for field in row:
        print(field, end = " ")
    print()

def print_word_table(wt):
    print("Words Occurrences Line Word# Line Word#")
  
for row in wt:
        print_row(row)

def main():
    file_name = "sentences.txt"
    wt = word_processor(file_name)
    print_word_table(wt)

main()



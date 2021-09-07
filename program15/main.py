import csv

def reader(filename: str, 
           rollno: str)->str:
    with open(filename, 'r') as toread:
        main = csv.reader(toread)
        val_list = [x for x in main]
        found = False
        for i in val_list:
            if i[0]==rollno:
                print(F'''
name:   {i[1]}                      
rollno: {i[0]}                      
class:  {i[2]}                      
                      ''')
                found = True
            else: pass
        print('No such student found') if not found else None

def writer(filename:str, 
           total_no_inputs: int)-> str:
    with open(filename, 'a', newline='') as jammer:
        main = csv.writer(jammer,
                          delimiter=',')
        for i in range(1,total_no_inputs+1): 
            print(F'Round {i}'+'-'*20)
            rollno, name, classstd = str(input('Enter empno: ')), str(input('Enter name: ')), str(input('Enter designation: '))
            main.writerow([rollno, name, classstd])
            print()
    

while True:
    x = str(input('Enter what ya wanna do(w/write, b/read, c/terminate): '))
    if x == 'w': writer('program15.csv', int(input('Enter the total no. of inputs ya wanna give: ')))
    elif x == 'b': reader('program15.csv', str(input('Enter the empno of the person.. whose details should be displayed: ')))
    elif x == 'c': 
        print('Thanks for choosing us!')
        break
    else: print('Oops! invalid input... Try again.')
    print()

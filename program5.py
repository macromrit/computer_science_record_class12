#program 5 - calculating % and marks of a stufent in 5 subjects
#wap to calculate % of a student in 5 subject

def class_grp(name: str="amrit", 
              sub1: int=100, 
              sub2: int=100, 
              sub3: int=100, 
              sub4: int=100, 
              sub5: int=100)->float and str:
              
    if 0<sub1<= 100 and 0<sub2<= 100 and 0<sub3<= 100 and 0<sub4<= 100 and 0<sub5<= 100:

        total_marks = sub1+sub2+sub3+sub4+sub5
        total_avg = total_marks/5
        total_per = ((total_avg/100)*100)
        print("the total percentage secured by student {0} is {1}".format(name, total_per))
    
    else:
        print("sorry did'nt work up great, values were misleading")

print("""

DISCLAIMER
this program is solely made for the purpose of computer science students

""")

name_pup = str(input("enter pupil's name: "))

sub_1 = int(input("input marks scored in computer science: "))

sub_2 = int(input("input marks scored in math: "))

sub_3 = int(input("input marks scored in physics: "))

sub_4 = int(input("input marks scored in chemistry: "))

sub_5 = int(input("input marks scored in english: "))

if __name__=="__main__":
    class_grp(name_pup, sub_1, sub_2, sub_3, sub_4, sub_5)
else:
    print("sorry something went wrong")
with open('program14.dat', 'r+b') as jammer:
    main_list = pickle.load(jammer)
    
founded = False
rollno = int(input('Enter the rollno whose marks should be updated: '))

for z in main_list: 
    if rollno == z[0]:
        founded = True
        break
    else: pass
    
if founded:    
    with open('program14.dat', 'w+b') as writables:
        updated_list = list()
        found = False
        for i in main_list:
            if i[0]==rollno: 
                found = True
                marks = int(input(F'Enter the updated marks of {i[2]}: '))
                i[1]=marks
            else: pass
            updated_list.append(i)
        pickle.dump(updated_list, writables)
        print('Data updated successfully!')
        
else: print('No such student was found')

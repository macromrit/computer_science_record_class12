import pickle

with open('program13.dat', 'r+b') as proceed:
    rollno = int(input('Enter the rollno\'s info to be displayed: '))
    found=False
    for i in pickle.load(proceed):
        if i[0]==rollno: 
            print(F'''
rollno = {i[0]} 
name   = {i[1]}
''')
            found=True
            break
        else: pass
    print('No such pupil was detected') if not found else None

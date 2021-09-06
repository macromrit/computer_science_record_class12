def hashprint(filename: str)->str:
    with open(filename, 'r') as blueorigin:
        print('#'.join(blueorigin.read().split()))
hashprint('program11.txt')

'''
output->
Jeff#flew#to#space#and#is#back#again#alive#XD
'''  

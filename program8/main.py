with open('count.txt', 'r') as jammer:
    jammerish = jammer.read()
    ans = jammerish.split()
    
    print(F"""
content from the txt file:
-----------------------------------
{jammerish}
-----------------------------------
    """)
    
    element = str(input('enter the element to be tallied: '))
    print(F"{element} was found {ans.count(element)} times")

    #if you type Amrit the output will be "Amrit was found 4 times"

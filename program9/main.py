with open('filter.txt', 'r') as jammer:
    ans = list()
    jammerish = jammer.readline()
    while jammerish:
        if jammerish[0]=='A':
            ans.append(jammerish.strip('\n'))
        else:
            pass
        jammerish = jammer.readline()

print('Lines starting with A were')
count = 1
for i in ans:
    print(F'{count} -> {i}')
    count+=1

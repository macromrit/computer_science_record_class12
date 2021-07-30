# #program 2 - Calculating sum of elements in a given list
# #wap to calculate sum of elements in a given list 
list_main = [1, 2, 3, 4, 5, 6]
val = 0
answer = 0

while val < len(list_main):
    answer += list_main[val]
    val+=1
print(answer)

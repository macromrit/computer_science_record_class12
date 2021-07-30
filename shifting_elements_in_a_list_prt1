#shifting elements in a list -> macromrit
x = eval(input('Enter an array comprised of integers: '))
scratch = dict()
count = 0 
while count<len(x):
    scratch[F'element{count}'] = (x[count], count, count-2)#element name, current index of the element, predicted index of the element
    count+=1
y = scratch.values()
main_list = list()
for i in y:
    main_list.append(i)
atlast = sorted(main_list, reverse=True)
upper_vals = list()
lower_vals = list()
for i in atlast:
    if i[2]>=0:
        upper_vals.append(i)
    else:
        lower_vals.append(i)
main_uper = sorted(upper_vals, key= lambda val : val[2])
ans_list = list()
for i in main_uper:
    ans_list.append(i[0])
for i in lower_vals[::-1]:
    ans_list.append(i[0])
print(F'The final ans is: {ans_list}')  

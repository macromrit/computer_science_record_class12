# #program 3 - appending in a list
# #appending elements to a list
list_root = []

while True:

    value = str(input("enter elements to be appended into the list list_root and input 'break' to leave the program: "))
    
    if value == "break":
        print("thanks for choosing us")
        break

    elif value in list_root:
        print("Oooops it seems the list already has this element")
    
    elif value not in list_root:
        print("Sounds valid! it has been appended")
        list_root.append(value)
        print('appendment successfull')
        print(list_root)
    
    else:
        print("sorry invalid input")
file1 = str(input("name of the file from which elements should be extracted[don't add .txt extension]: "))
file2 = str(input("name of the file from which elements should be appended from the extracted file[don't add .txt extension]: "))

with open(F'{file1}.txt', 'r') as jammerish:
    main = jammerish.readlines()
    final_1 = jammerish.read()
    app_list = list()
    for i in main:
        if (i[0].islower()):
            app_list.append(i)
        else:
            pass
    
    with open(F'{file2}.txt', 'w+') as blaberish:
        for i in app_list:
            print(i.strip('\n'),file=blaberish)
        final_2 = blaberish.read()

print(F'Elements appended to file {file2} were:')
for i in app_list:
    print(i.strip('\n'))
    
#assuming that the user inputs file1 and file2 as input

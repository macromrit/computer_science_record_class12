# #program 1 - Palindrome
# #wap to check whether a string is pallindrome or not
while True:
    try:
        term = str(input("enter the term to find whether its palindrome or not: ")).casefold()
        ######div1
        break
        ######div2

    except(EOFError, KeyboardInterrupt):
        print("sorry it didnt work! try again")      

term_reversed = term[::-1]

if term == term_reversed:
    print(F"""
% this program is not case sensitive %
Yes! the term you inputed is a palindrome
term               = {term}
palindrome of term = {term_reversed}    
    """)

else:
    print("oppps! no it did'nt work well, not a palindrome")

def chr_tally(filename: str)->str:
    with open(filename, 'r') as count:
        vals = {'upper': 0,
                'lower': 0,
                'consonants': 0,
                'vowels': 0,
                'non-alpha': 0}
        
        for chr in count.read():
            if chr.isalpha():
                
                if chr.isupper(): 
                    if chr in list('AEIOU'): vals['vowels']+=1
                    elif chr not in list('AEIOU'): vals['consonants']+=1
                    else: pass
                    vals['upper']+=1
                    
                elif chr.islower():
                    if chr in list('aeiou'): vals['vowels']+=1
                    elif chr not in list('aeiou'): vals['consonants']+=1
                    else: pass
                    vals['lower']+=1
                
                else: pass
            
            else: vals['non-alpha']+=1
    
    print(F'''
          upper_case               = {vals['upper']}
          lower_case               = {vals['lower']}
          vowels                   = {vals['vowels']}
          consonants               = {vals['consonants']}
          non-alpha[space&stuffs]  = {vals['non-alpha']}
          ''')
    
chr_tally('program12.txt')

'''
output->
    upper_case               = 1
    lower_case               = 56
    vowels                   = 23
    consonants               = 34
    non-alpha[space&stuffs]  = 13
'''

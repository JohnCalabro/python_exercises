def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
   # In [297]: {num: num * num for num in range(1,10) if num % 2 == 0}
# Out[297]: {2: 4, 4: 16, 6: 36, 8: 64}
    phrase = phrase.lower()
    print(phrase)
    vows = 'aeiou'
    return {lett: phrase.count(lett) for lett in phrase if lett in vows}



    

        



    
    
    
           
        
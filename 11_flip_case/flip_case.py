def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out
    
# ^ I get it. Second argument if it's capitalized will be lowercased first, we then initialie
# an empty str so we can add onto it. Then we loop through each char in the phrase and check
# if our char in the phrase (we make lower case for checking purposes) is the same val is our
# second argument (the letter we are checking) we switch it's casing and add each letter in the 
# loop to populate our empty string to get a new one


    


        

    
 

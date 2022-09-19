def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_word = ""

    for ltr in phrase:
        if ltr == to_swap:
            new_word = new_word + ltr.swapcase()
        
        elif ltr == to_swap.upper():
            new_word = new_word + ltr.swapcase()
        
        elif ltr == to_swap.lower():
            new_word = new_word + ltr.swapcase()
        
        else: 
            new_word = new_word + ltr

    return new_word
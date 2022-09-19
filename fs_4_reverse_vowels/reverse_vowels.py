from audioop import reverse


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    VOWELS = "aeiou"
    vowels_in_s= []
    final_word =""
    
    for ltr in s:
        if ltr in VOWELS:
           vowels_in_s.append(ltr)

    # reverse_vowels = vowels_in_s[::-1]  
    
    for ltr in s:

        # if ltr is not VOWELS:
        #     final_word += ltr
        if ltr in VOWELS:
            final_word += vowels_in_s.pop()
            # for i in range(len(reverse_vowels)):
            #     final_word += reverse_vowels[i]
        else:
            final_word += ltr
    return final_word
    
    
    print(vowels_in_s)
    print(reverse_vowels)
    print(final_word)


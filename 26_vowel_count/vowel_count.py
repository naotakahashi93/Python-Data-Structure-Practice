def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    VOWELS = "aeiou"
    return_dict = {}

    for letter in phrase: # for each letter in the phrase
        if letter in VOWELS: #if the letter is included in the VOWELS string
            return_dict[letter] = return_dict.get(letter,0) + 1 #we add one to the value of that letter key, if that key does not exist we set the initial value to 0
    

    return return_dict 
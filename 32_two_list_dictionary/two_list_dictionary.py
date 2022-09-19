import difflib


def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    return_dict = {}

    for idx in range(0,len(keys)): #looping through numbers 0-length of keys to get index
        if len(keys) == len(values):
            for key in keys[idx]: #by getting the key in the first index of keys list
                return_dict[key] = values[idx] #we can assign a value from the values list to that same index 
      

    return return_dict
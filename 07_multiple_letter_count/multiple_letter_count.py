from itertools import count


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter_dict = {}

    for ltr in phrase:
        if ltr in counter_dict:
            counter_dict[ltr] = counter_dict[ltr]+1 
        else:
            counter_dict[ltr] = 1

    return counter_dict
from itertools import count


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

  
    counter = {}  # "counter" is a dictionary where key is the element in the list and the value is the number of times it appears

    for num in nums:
        if num in counter:
            counter[num] = counter[num]+1

        else:
            counter[num] = 1
    
    max_val = max(counter.values()) #will return the highest number in the counter.values which is the number that occurs the most

    for (key, value) in counter.items():
        if value == max_val:
            return key
def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    counter_obj = {}
    for num in nums:
        counter_obj[num] = counter_obj.get(num,0) +1
      
    
    for (key, value) in counter_obj.items():
        if value >= 2:
            return key
    





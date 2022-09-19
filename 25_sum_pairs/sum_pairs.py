def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    initial_num = set() # first starting out with an empty set

    for num in nums: #looping over each number in the nums list
        diff = goal - num # setting a variable for that requires us to get the difference between the goal and the num we have 

        if diff in initial_num: # if the diff we need is in the initial_num set we return that number and the num we have
            return (diff, num)

        initial_num.add(num) # we add the num we have in the initial_num list

    return () # return empty tuple if there is none that reach the goal
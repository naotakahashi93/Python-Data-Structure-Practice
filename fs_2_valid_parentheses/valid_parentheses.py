def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    left_paren = 0
    right_paren = 0 

    for char in parens:
        if char == "(" :
            left_paren += 1
        
        if char == ")":
            right_paren += 1

    if left_paren == right_paren:
        return True

    else:
        return False 


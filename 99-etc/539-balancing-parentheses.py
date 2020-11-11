"""
539 Balancing Parentheses
    It's from the developer 539.

    Given a string that consists of left and right parentheses, '(' and ')',
    balance the parentheses by inserting parentheses as necessary.
    Determine the minimum number of characters that must be inserted.

    Example
        s = '(()))'
    
    Insert 1 left parenthesis at the left end of the string to get '((()))'.
    The string is balanced after 1 insertion
"""
def count_required_parentheses(s):
    while '()' in s:
        s = s.replace('()', '')
    return len(s)

def count_required_parentheses2(s):
    left = 0
    right = 0
    for ch in s:
        if ch == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1
    
    return left + right
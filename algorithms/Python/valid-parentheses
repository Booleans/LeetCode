'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

# Time: O(n)
# Space: O(n)

def isValid(s):
    '''
    :type s: str
    :rtype: bool
    '''
    if len(s) < 2:
        return False
    
    opening = tuple('([{')
    closing = tuple(')]}')
    mapper = dict(zip(opening, closing))
    stack = []

    for char in s:
        if char in opening:
            stack.append(mapper[char])
        elif (len(stack) == 0) or (char != stack.pop()):
            return False
    # If the loop has terminated and we have nothing left on the stack then return True.
    return len(stack) == 0
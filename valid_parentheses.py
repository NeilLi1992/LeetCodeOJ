# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def isValid(s):
    left = ['(','{','[']
    right = [')','}',']']
    stack = []
    for e in s:
        if e in left:
            stack.append(e)
        elif e in right:
            if stack == [] or left[right.index(e)] != stack.pop():
                # Right bracket closes a left one
                return False
        else:
            # Input is invalid
            return False

    return stack == []

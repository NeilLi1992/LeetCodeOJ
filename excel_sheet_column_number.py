# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

def titleToNumber(s):
    l = list(s)
    l.insert(0,0)
    return reduce(lambda x,y: 26*x+ord(y)-64, l)

    # total = 0
    # for i,c in enumerate(s):
    #     total += (ord(c.upper()) - 64) * pow(26, len(s)-i-1)
    #
    # return total
print titleToNumber("AA")

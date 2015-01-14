# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#

def convert(s, nRows):
    # if nRows == 1:
    #     return s
    # m = [[] for i in range(nRows)]
    # i = 0
    # delta = 1
    # for char in s:
    #     m[i].append(char)
    #     i += delta
    #     if i == nRows:
    #         i -= 2 * delta
    #         delta = -1
    #     elif i == -1:
    #         i += 2
    #         delta = 1
    # return "".join([item for sublist in m for item in sublist])

    # Another solution with itertools
    from itertools import cycle, izip, chain
    base_sequence = chain(range(nRows), range(nRows - 2, 0, -1))
    m = [[] for i in range(nRows)]

    # Distribute the char into the list of list
    for char,index in izip(s, cycle(base_sequence)):
        m[index].append(char)

    # Get a flat list from the list of list
    return "".join([item for sublist in m for item in sublist])


s = ("PAYPALISHIRING")
row = 3
print convert(s,row)

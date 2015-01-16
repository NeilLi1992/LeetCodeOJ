# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
def convertToTitle(num):
    title = []
    
    while num:
        i = (num - 1) % 26
        title.insert(0, str(unichr(i + 65)))
        num = (num - 1) / 26

    return "".join(title)

print convertToTitle(26)

# Write a function to find the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""

    if len(strs) < 2:
        return strs[0]

    # Sort array based on string length
    strs.sort(lambda x,y: cmp(len(x), len(y)))
    
    prefix = ""
    rest_strs = strs[1:]
    for i,c in enumerate(strs[0]):
        if all(s[i] == c for s in rest_strs):
            prefix += c
        else:
            return prefix

    return prefix

strs = [
        "aca",
        "cba",
        ]

print longestCommonPrefix(strs)

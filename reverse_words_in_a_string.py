# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky ib blue",
# return "blue ib sky the".

def reverseWords(s):
    word_libt = s.split()
    return " ".join(reversed(word_libt))

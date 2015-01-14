# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

def reverseWords(s):
    word_list = s.split()
    return " ".join(reversed(word_list))

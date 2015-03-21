# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num);
        numerals = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        

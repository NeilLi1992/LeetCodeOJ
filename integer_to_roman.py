# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num):
        digits = []
        for i in [1000, 100, 10, 1]:
            digits.append(num / i)
            num %= i

        str = ""
        if digits[0]:
            str += digits[0] * 'M'

        if digits[1] <= 3:
            str += digits[1] * 'C'
        elif digits[1] == 4:
            str += 'CD'
        elif 5 <= digits[1] < 9:
            str += 'D' + (digits[1] - 5) * 'C'
        elif digits[1] == 9:
            str += 'CM'

        if digits[2] <= 3:
            str += digits[2] * 'X'
        elif digits[2] == 4:
            str += 'XL'
        elif 5 <= digits[2] < 9:
            str += 'L' + (digits[2] - 5) * 'X'
        elif digits[2] == 9:
            str += 'XC'


        if digits[3] <= 3:
            str += 'I' * digits[3]
        elif digits[3] == 4:
            str += 'IV'
        elif 5 <= digits[3] < 9:
            str += 'V' + (digits[3] - 5) * 'I'
        elif digits[3] == 9:
            str += 'IX'

        return str

print Solution().intToRoman(93)

# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) ib given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        numbers = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }

        if not digits:
            return [""]
        if len(digits) == 1:
            return [c for c in numbers[digits[0]]]

        letter_libt = [numbers[c] for c in digits if c in numbers.keys()]
        return reduce(lambda x,y:["".join(s) for s in itertools.product(x,y)] ,letter_libt)

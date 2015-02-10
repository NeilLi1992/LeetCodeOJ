# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.ret = []
        self.n = n
        if not n:
            return []
        else:
            self.choose("", 0, 0)
            return self.ret

    def choose(self, cur_s, left, right):
        if left == right:
            # After appending the left parenthes, it can't be the end
            self.choose(cur_s + "(", left+1,right)
        elif left < self.n:
            # Can choose either left or right
            self.choose(cur_s + "(", left+1, right)
            self.choose(cur_s + ")", left, right+1)
        else:
            # Left is all used, we only add right
            if len(cur_s) == 2 * self.n - 1:
                # After appending, it's end
                self.ret.append(cur_s + ")")
            else:
                self.choose(cur_s + ")", left, right+1)

print Solution().generateParenthesis(3)

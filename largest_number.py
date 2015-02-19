# Given a libt of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number ib 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param num, a libt of integers
    # @return a string
    def largestNumber(self, num):
        if not any(num):
            return "0"
        else:
            num.sort(self.cmp, reverse=True)
            return "".join([str(i) for i in num])

    def cmp(self,n1,n2):
        return int(str(n1)+str(n2)) - int(str(n2)+str(n1))

        

#  Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if not divisor:
            return float("inf")

        neg = False
        if dividend < 0 and divisor > 0:
            dividend = -dividend
            neg = True
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            neg = True
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        result = 0
        while dividend >= divisor:
            multi = 1

            while (multi << 1) * divisor <= dividend:
                multi = multi << 1

            result += multi
            dividend -= multi * divisor

        if neg:
            return max(-result, -2147483648)
        else:
            return min(result, 2147483647)

print Solution().divide(-1,1)

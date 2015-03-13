# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if not x:
            return 0
        elif x == 1:
            return 1
        else:
            low = 0.0
            high = x * 1.0
            mid = (low + high) / 2.0
            error = 0.000001

            while abs(mid * mid - x) > error:
                if mid * mid > x:
                    high = mid
                    mid = (low + high) / 2.0
                else:
                    low = mid
                    mid = (low + high) / 2.0

            return int(mid)


print Solution().sqrt(1)

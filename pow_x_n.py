# Implement pow(x, n).

class Solution():
    def pow(self, x, n):
        # @param x, a float
        # @param n, a integer
        # return a float
        if n > 0:
            return self.power(x, n)
        else:
            return 1 / self.power(x, -n)

    def power(self, x, n):
        if n == 1:
            return x * 1.0

        if n == 0:
            return 1.0

        temp = self.power(x, n / 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x

print Solution().pow()

# Description:
#
# Count the number of prime numbers less than a non-negative number, n
#
# Hint: The number n could be in the order of 100,000 to 5,000,000.

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        return sum([1 for i in xrange(n) if self.isPrime(i)])

    def isPrime(self, n):
        if n < 2:
            return False

        for i in xrange(2, (int)(pow(n,0.5)) + 1):
            if n % i == 0:
                return False
        else:
            return True

class Solution2:
    def countPrimes(self, n):
        if n < 2:
            return 0

        isPrime = [True for i in xrange(n)]
        isPrime[0] = isPrime[1] = False

        # Test all Primes less than sqrt(n)
        i = 2
        while i ** 2 < n:
            if isPrime[i]:
                multiplier = 0
                while i ** 2 + i * multiplier < n:
                    isPrime[i ** 2 + i * multiplier] = False

                    multiplier += 1
            i += 1

        return sum(isPrime)

import math
class Solution3:
    def countPrimes(self, n):
        if n < 2:
            return 0

        count = n - 2 # exclude 1, n
        i = 2

        while i ** 2 < n:
            if self.isPrime(i):
                count -= math.ceil(1.0 * (n - i ** 2) / i)
                # count -= (n - i ** 2) // i
                print "i = {}, (n-i^2)//i={}, count={}".format(i, (n - i ** 2) // 2, count)

            i += 1

        return int(count)

    def isPrime(self, n):
        if n < 2:
            return False

        for i in xrange(2, (int)(pow(n,0.5)) + 1):
            if n % i == 0:
                return False
        else:
            return True

print Solution2().countPrimes(999983)

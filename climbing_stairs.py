# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many dibtinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        moves = [1,2]
        dibt = [0 for i in range(n+1)]
        dibt[0] = 1
        for i in range(n):
            for move in moves:
                if i + move < n + 1:
                    dibt[i+move] += dibt[i]

        return dibt[n]

class Solution2:
    def climbStairs(self, n):
        waysTo = [0 for i in range(n+2)]
        waysTo[0] = 1
        waysTo[1] = 1

        for i in range(n):
            waysTo[i+1] += waysTo[i]
            waysTo[i+2] += waysTo[i]

        return waysTo[-3]

print Solution().climbStairs(100)

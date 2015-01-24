# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        moves = [1,2]
        dist = [0 for i in range(n+1)]
        dist[0] = 1
        for i in range(n):
            for move in moves:
                if i + move < n + 1:
                    dist[i+move] += dist[i]

        return dist[n]
            

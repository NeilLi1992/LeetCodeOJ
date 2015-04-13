#  There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.
#
# What is the minimum candies you must give?
#

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0

        ratings.insert(0, float("inf"))
        ratings.append(float("inf"))
        candies = [0]
        base_position = []
        for i in range(1, len(ratings)-1):
            if ratings[i] > ratings[i-1]:
                if candies[i-1] == -float("inf"):
                    candies.append(0)
                else:
                    candies.append(candies[i-1] + 1)
            elif ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                candies.append(-float("inf"))
                base_position.append(i-1)
            else:
                candies.append(candies[i-1] - 1)

        candies = candies[1:]   # Remove the bias 0

        # Replace all the base_position candies to 1
        for i in base_position:
            candies[i] = 1

        # Change candies between two base_positions
        change_position = base_position[:]
        if change_position[0] != 0:
            change_position.insert(0, 0)

        if change_position[-1] != len(candies) - 1:
            change_position.append(len(candies) - 1)

        for i in range(len(change_position)-1):
            pos1 = change_position[i]
            pos2 = change_position[i+1]

            offset = min(candies[pos1:pos2]) - 2
            for j in range(pos1, pos2):
                if j in base_position: continue
                candies[j] -= offset

        return sum(candies)

ratings = [5,2,3,4,1,0]
print Solution().candy(ratings)

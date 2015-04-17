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

class Solution2:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1

        ratings.insert(0, float("inf"))
        ratings.append(float("inf"))
        candies = [0 for _ in range(len(ratings))]

        run_min = float("inf")
        run_index = 0
        for i in range(1, len(candies)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                print candies, run_min, run_index
                # This is a local minimum position
                candies[i] = 1
                # Adjust candies [run_index, i)
                offset = run_min - 2
                if offset:
                    for j in range(run_index, i):
                        candies[j] -= offset
                run_index = i + 1
                run_min = float("inf")
            else:
                if ratings[i] <= ratings[i-1]:
                    candies[i] = candies[i-1] - 1
                elif ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
                    run_index = i
                else:
                    # ratings[i] == ratings[i-1]
                    candies[i] = candies[i-1]

                if candies[i] < run_min:
                    run_min = candies[i]

        if run_index == 0:
            offset = run_min - 1
            for i in range(1, len(candies)-1):
                candies[i] -= offset

        print candies
        return sum(candies[1:])

class Solution3:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1

        ratings.insert(0, float("inf"))
        ratings.append(float("inf"))
        candies = [0 for _ in range(len(ratings))]

        bas_pos = []

        for i in range(1, len(ratings)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                bas_pos.append(i)

        # print "bas_pos = ", bas_pos

        for i in range(len(bas_pos)):
            candies[bas_pos[i]] = 1

        # print "candies = ", candies

        # Calculate each bas_pos ranges
        if len(bas_pos) > 1:
            for i in range(len(bas_pos)-1):
                base1 = bas_pos[i]
                base2 = bas_pos[i+1]

                if base2 - base1 < 2:
                    continue

                run_max = -float("inf")
                run_index = -1
                for j in range(base1+1, base2):
                    if ratings[j] > run_max:
                        run_max = ratings[j]
                        run_index = j

                # if base1 == 17:
                #     import pdb; pdb.set_trace()
                for j in range(base1+1, run_index):
                    candies[j] = candies[j-1] + 1 if ratings[j] > ratings[j-1] else ratings[j-1]

                for j in range(base2-1, run_index, -1):
                    candies[j] = candies[j+1] + 1 if ratings[j] > ratings[j+1] else ratings[j+1]

                if ratings[run_index] == ratings[run_index+1]:
                    candies[run_index] = candies[run_index+1]
                    if candies[run_index] <= candies[run_index-1]:
                        candies[run_index] = candies[run_index-1] + 1
                else:
                    candies[run_index] = max(candies[run_index-1], candies[run_index+1]) + 1

                # if ratings[run_index] == ratings[run_index+1]:
                #     candies[run_index] = candies[run_index+1]
                # elif ratings[run_index] == ratings[run_index-1]:
                #     candies[run_index] = candies[run_index-1]
                # else:
                #     candies[run_index] = max(candies[run_index-1], candies[run_index+1]) + 1

        # Calculate the starting positions
        if bas_pos[0] != 0:
            for i in range(bas_pos[0]-1, -1, -1):
                candies[i] = candies[i+1] + 1

        # Calculate thte ending positions
        if bas_pos[-1] != len(ratings) - 1:
            for i in range(bas_pos[-1]+1, len(ratings)):
                candies[i] = candies[i-1] + 1

        # print candies
        # print ratings[16], ratings[17], ratings[18]
        # print candies[16], candies[17], candies[18]
        # print candies
        return sum(candies[1:-1])

# ratings = [5,2,3,4,0,1,7,5,8]
# ratings = [2,2]
ratings = [58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89]



print Solution3().candy(ratings)

my_answer = [3, 2, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 2, 1, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 5, 2, 1, 3, 2, 1, 2, 3, 4, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 3, 4, 5, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4]

# answer =    [3, 2, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 3 3 2 1 2 3 4 5 2 1 3 2 1 2 3 4 1 2 1 2 1 2 3 2 1 2 1 2 3 4 5 1 2 1 2 3 2 1 2 1 2 1 2 1 2 1 2 1 2 3 2 1 2 1 2 1 2 3 4 5 1 2 3 1 2 3 4 1 2 3,4]

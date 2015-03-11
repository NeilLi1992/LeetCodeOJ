#  There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.
#

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        for start in range(len(gas)):
            tank = 0
            travel_list = range(len(gas))[start:] + range(len(gas))[:start]
            can_travel = True
            for from_pos in travel_list:
                tank += gas[from_pos]
                if tank < cost[from_pos]:
                    can_travel = False
                    break
                else:
                    tank -= cost[from_pos]
            if can_travel:
                return start
        else:
            return -1

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

class Solution2:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        travel_list = 2 * range(N)
        start = tank = 0
        for i, station in enumerate(travel_list):
            tank += gas[station]
            tank -= cost[station]
            if tank >= 0 and travel_list[i+1] == start:
                # Find the start index
                return start
            elif tank < 0:
                if i+1 > travel_list[i+1]:
                    # Won't find any more
                    return -1
                else:
                    tank = 0
                    start = travel_list[i+1]

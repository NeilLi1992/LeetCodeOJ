# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        letter_list = [chr(x) for x in range(97,123)]
        visited = {end:False}

        for e in dict:
            visited[e] = False

        queue = []
        dict.add(end)
        for i in range(len(start)):
            c = start[i]
            for letter in letter_list:
                if c == letter:
                    continue
                temp = start[0:i] + letter + start[i+1:]
                if temp in dict:
                    queue.insert(0, (temp,2))
                    visited[temp] = True

        # time2 = clock()
        # print (time2 - time1)

        while queue:
            # print queue
            node,length = queue.pop()
            if node == end:
                print "found"
                return length
            else:
                for i in range(len(node)):
                    c = node[i]
                    for letter in letter_list:
                        if c == letter:
                            continue
                        temp = node[0:i] + letter + node[i+1:]
                        if temp in dict and not visited[temp]:
                            queue.insert(0, (temp,length+1))
                            visited[temp] = True
        return 0

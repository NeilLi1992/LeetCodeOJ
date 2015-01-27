# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

# This is my original implementation, but it's quite slow
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 1:
            # This is a single-character palindrome string
            return [[s]]
        else:
            partition_list = []

            if s == s[::-1]:
                partition_list.append([s])

            for i in range(1,len(s)):
                s1 = s[0:i]
                s2 = s[i:len(s)]

                if s1 != s1[::-1]: # s1 is not palindrome, this partition failed
                    continue
                else: # The first substring is a palindrom
                    substr_par_list = self.partition(s2)
                    for substr_par in substr_par_list:
                        substr_par.insert(0, s1)
                        partition_list.append(substr_par)
            return partition_list

# Second solution uses DP+dfs
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        index_list = [[] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    index_list[i].append(j)

        partition_list = []
        self.search_path(0, [], index_list, s, partition_list)
        return partition_list

    def search_path(self, start, current_partition, index_list, s, partition_list):
        for end in index_list[start]:
            new_partition = current_partition[:]
            new_partition.append(s[start:end+1])

            if end + 1 == len(s):
                partition_list.append(new_partition)
            else:
                self.search_path(end+1, new_partition, index_list, s, partition_list)

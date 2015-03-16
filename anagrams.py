# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#

class Solution():
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        look_up = {}
        for s in strs:
            hash_num = hash(tuple(sorted(list(s))))
            if hash_num in look_up:
                look_up[hash_num].append(s)
            else:
                look_up[hash_num] = [s]

        to_return = []
        for k, l in look_up.iteritems():
            if len(l) > 1:
                to_return.extend(l)

        return to_return

# input = ['abc', 'cba', 'dkf']
# input = [""]
input = ["tea","and","ate","eat","dan"]
print Solution().anagrams(input)

#  All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if len(s) < 11:
            return []

        hash_table = {}

        for i in range(len(s) - 9):
            sub_s = s[i:i+10]

            if sub_s in hash_table:
                hash_table[sub_s] += 1
            else:
                hash_table[sub_s] = 1

        result = []
        for k, v in hash_table.iteritems():
            if v > 1:
                result.append(k)

        return result

s = "AAAAAAAAAAA"
print Solution().findRepeatedDnaSequences(s)

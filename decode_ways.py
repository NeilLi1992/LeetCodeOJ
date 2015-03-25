#  A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        self.ret = 0
        self.decode(s)
        return self.ret

    def decode(self, s):
        if len(s) == 0:
            return
        if len(s) == 1:
            self.ret += 1
            return
        elif 1 <= int(s[:2]) <= 26:
            self. ret += 2
            self.decode(s[1:])
            self.decode(s[2:])

class Solution2:
    def numDecodings(self, s):
        if not s:
            return 0

        s = '9' + s
        book = [0 for i in range(len(s))]
        book[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                if 11<= int(s[i-1:i+1]) <= 26:
                    book[i] = book[i-2] + book[i-1]
                else:
                    book[i] = book[i-1]
            else:
                if s[i-1] == '0' or int(s[i-1]) > 2:
                    # This 0 can't be deciphered
                    return 0
                else:
                    book[i] = book[i-2]

        return book[-1]

s = "1102"
print Solution2().numDecodings(s)

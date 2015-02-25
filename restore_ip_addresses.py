# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution:
    # @param s, a string
    # @ return a list of strings
    def restoreIpAddresses(self, s):
        if not s.isdigit() or len(s) > 12 or len(s) < 4:
            return []
        else:
            ret = []
            char_list = list(s)
            for i in range(1, 4):
                s1 = "".join(char_list[:i])
                if not 0 <= int(s1) <= 255:
                    continue
                if s1[0] == '0' and len(s1) > 1:
                    continue
                for j in range(i+1, min(len(s) - 1, i+4)):
                    s2 = "".join(char_list[i:j])
                    if not 0 <= int(s2) <= 255:
                        continue
                    if s2[0] == '0' and len(s2) > 1:
                        continue
                    for k in range(j+1, min(len(s), j+4)):
                        s3 = "".join(char_list[j:k])
                        s4 = "".join(char_list[k:])
                        if not 0 <= int(s3) <= 255 or not 0 <= int(s4) <= 255:
                            continue
                        elif (s3[0] == '0' and len(s3) > 1) or (s4[0] == '0' and len(s4) >1):
                            continue
                        else:
                            ret.append(".".join([s1,s2,s3,s4]))
            return ret

s = "010010"
print Solution().restoreIpAddresses(s)

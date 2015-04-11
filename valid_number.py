# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

# The easy way
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

# The harder way
class Solution2:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        s = s.lower()
        dot_seen = False
        e_seen = False

        e_list = s.split("e")

        # Contain more than 1 e: 1e1e
        if len(e_list) > 2:
            return False
        elif len(e_list) == 2:  # Contain 1 e
            # No number after e: 23e
            if not e_list[1]:
                return False

            if e_list[1][0] == "+" or e_list[1][0] == "-":
                e_list[1] = e_list[1][1:]

            # e number contains no digit
            for i,c in enumerate(e_list[1]):
                if ord(c) < 48 or ord(c) > 57:
                    return False

        else:   # No e
            # Contain more than 1 dot
            dot_list = e_list[0].split(".")

            # Contain more than 1 dot:
            if len(dot_list) > 2:
                return False

            if e_list[0].count(".") > 1:
                return False

            if e_list[0][0] == "+" or e_list[0][0] == "-":
                e_list[0] = e_list[0][1:]

            for i, c in enumerate(e_list[0]):
                if (ord(c) < 48 or ord(c) > 57) and c != ".":
                    return False

        return True

print Solution2().isNumber("3.e")

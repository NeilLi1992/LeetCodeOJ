# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
#     Given numerator = 1, denominator = 2, return "0.5".
#     Given numerator = 2, denominator = 1, return "2".
#     Given numerator = 2, denominator = 3, return "0.(6)".

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        neg = False
        digit_nume_list = []
        repeating_index = None

        if numerator * denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            neg = True

        while True:
            digit = numerator // denominator
            remainder = numerator % denominator

            if remainder == 0:
                digit_nume_list.append((digit, numerator))
                break
            elif (digit, numerator) in digit_nume_list:
                repeating_index = (digit_nume_list.index((digit, numerator)), len(digit_nume_list))
                break
            else:
                digit_nume_list.append((digit, numerator))
                numerator = remainder * 10

        if repeating_index:
            assert repeating_index[0] > 0, "Int part is repeating"
            digit_nume_list.insert(repeating_index[0], "(")
            digit_nume_list.append(")")
            digit_nume_list.insert(1, ".")
            if neg:
                digit_nume_list.insert(0, "-")
            return "".join([str(t[0]) for t in digit_nume_list])
        else:
            if len(digit_nume_list) == 1:
                if neg:
                    digit_nume_list.insert(0, "-")
                return "".join([str(t[0]) for t in digit_nume_list])
            else:
                digit_nume_list.insert(1, ".")
                if neg:
                    digit_nume_list.insert(0, "-")
                return "".join([str(t[0]) for t in digit_nume_list])

numerator = -2147483648
denominator = 1
print Solution().fractionToDecimal(numerator, denominator)

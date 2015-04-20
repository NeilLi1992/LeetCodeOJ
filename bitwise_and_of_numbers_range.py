# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.

# Basic naive solution
# Didn't pass the test case [0, 2147483647]
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        r = m
        for i in range(m, n+1):
            r = r & i
        return r

class Solution2:
    def rangeBitwiseAnd(self, m, n):
        bit_len_m = len(bin(m)) - 2
        bit_len_n = len(bin(n)) - 2
        max_bit_len = max(bit_len_m, bit_len_n)
        bin_result = ""

        # Zero offset
        m = m + 1
        n = n + 1
        for i in range(max_bit_len):
            cycle_num = 2 ** (max_bit_len - i)

            one_before_m = 0
            one_before_m += m // cycle_num * (cycle_num / 2)
            remainder_m = m % cycle_num
            if remainder_m > cycle_num / 2:
                one_before_m += remainder_m - cycle_num / 2

            np1 = n + 1
            one_before_np1 = 0
            one_before_np1 += np1 // cycle_num * (cycle_num / 2)
            remainder_np1 = np1 % cycle_num
            if remainder_np1 > cycle_num / 2:
                one_before_np1 += remainder_np1 - cycle_num / 2

            # This is wrong !!!! This is doing bitwise negation!!

class Solution3:
    def rangeBitwiseAnd(self, m, n):
        bin_str_m = bin(m)
        bin_str_n = bin(n)
        bit_len_m = len(bin_str_m) - 2
        bit_len_n = len(bin_str_n) - 2
        min_bit_len = min(bit_len_m, bit_len_n)
        result_list = []

        for i in range(min_bit_len):
            cycle_num = 2 ** (min_bit_len - i)

            if bin_str_m[-min_bit_len:][i] == bin_str_n[-min_bit_len:][i] == "1" and (n - m + 1) <= cycle_num / 2:
                result_list.append("1")
            else:
                result_list.append("0")

        return int("".join(result_list), base=2)


# print Solution().rangeBitwiseAnd(0,2147483647)
print Solution3().rangeBitwiseAnd(5,7)

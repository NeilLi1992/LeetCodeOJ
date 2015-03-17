# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        mul_table = [[i*j for i in range(10)] for j in range(10)]
        add_table = [[i+j for i in range(10)] for j in range(10)]

        bitwise_mul = []
        padding_count = 0
        for j in reversed(range(len(num2))):
            digit2 = int(num2[j])
            result = []
            carry = 0

            result.extend(['0' for i in range(padding_count)])

            for i in reversed(range(len(num1))):
                digit1 = int(num1[i])
                one_bit_mul = mul_table[digit1][digit2] + carry
                result.append(str(one_bit_mul % 10))
                carry = one_bit_mul / 10
            if carry:
                result.append(str(carry))

            bitwise_mul.append("".join(result))
            padding_count += 1

        cal_result = []
        carry = 0
        for i in range(len(bitwise_mul[-1])):
            bit_add_result = 0
            for add_str in bitwise_mul:
                if i < len(add_str):
                    bit_add_result += int(add_str[i])
            bit_add_result += carry
            carry = bit_add_result / 10
            cal_result.append(bit_add_result % 10)

        if carry:
            for digit in reversed(list(str(carry))):
                cal_result.append(int(digit))

        i = len(cal_result) - 1
        while i > 0:
            if cal_result[i] != 0:
                break
            else:
                del cal_result[i]
                i -= 1

        print cal_result
        return "".join([str(i) for i in reversed(cal_result)])



print Solution().multiply("999", "0")

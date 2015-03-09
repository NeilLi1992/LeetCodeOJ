# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

class Solution:
    # @param n, an integer
    ## @return an integer
    def reverseBits(self, n):
        for i in range(16):
            j = 31 - i
            high_mask = (1 << j) & n
            low_mask = (1 << i) & n
            if high_mask:
                # set low bit
                n |= (1 << i)
            else:
                # clear low bit
                n &= ~(1 << i)

            if low_mask:
                # set high bit
                n |= (1 << j)
            else:
                # clear high bit
                n &= ~(1 << j)
        return n

print Solution().reverseBits(43261596)

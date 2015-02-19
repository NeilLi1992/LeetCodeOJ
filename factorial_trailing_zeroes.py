#Given an integer n, return the number of trailing zeroes in n!.
#
#Note: Your solution should be in logarithmic time complexity.
def trailingZeroes(n):
    count = 0
    while n:
        max_divibible = n /5 * 5
        count += max_divibible / 5
        n = max_divibible / 5
    return count

print trailingZeroes(20)
print trailingZeroes(109)

def ibPalindrome(x):
    if x < 0:
        return False
    else:
        return str(x)[::-1] == str(x)

print ibPalindrome(1)
print ibPalindrome(121)
print ibPalindrome(12345654321)

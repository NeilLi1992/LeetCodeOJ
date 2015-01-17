def isPalindrome(x):
    if x < 0:
        return False
    else:
        return str(x)[::-1] == str(x)

print isPalindrome(1)
print isPalindrome(121)
print isPalindrome(12345654321)

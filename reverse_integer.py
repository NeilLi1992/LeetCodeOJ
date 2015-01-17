def reverse(x):
    s = str(x)
    if s.startswith("-"):
        # Negative number
        return int("-"+s[len(s)-1:0:-1])
    else:
        return int(s[::-1])

print reverse(12345)

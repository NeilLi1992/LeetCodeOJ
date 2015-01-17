#Implement atoi to convert a string to an integer.
#
#Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
#Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
def atoi(s):
    # Remove white spce
    s = s.strip()
    nums = [str(i) for i in range(10)]
    num = 0
    sign = 1
    if s[0] == "-":
        sign = -1
        s  = s[1:]
    elif s[0] == "+":
        s = s[1:]
    print s 
    for c in s:
        if c in nums:
            print c
            num = num * 10 + int(c)
        else:
            break
    return num * sign

test_case = {
            123:["123","+123","0123","00123"],
            0:["0","0","+0","-0"],
            -123:["-123", "-123"],
            10:["     010"],
        }

#if __name__ == "__main__":
#    for n,l in test_case.items():
#        print n,l
#        for s in l:
#            if atoi(s) != n:
#                print "Failed at n=%d,s=%s" % (n,s)
#
#    print "Accepted"
print atoi("         010")

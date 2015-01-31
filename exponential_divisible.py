# Given an integer can we find if it can be expressed in form of p^q

def func(num):
    for p in range(2, int(num ** 0.5) + 1):
        q = 1
        temp = p
        while temp < num:
            temp *= p
            q += 1
        if temp == num:
            print "Found %d=%d^%d" % (num,p,q)

func(390625)

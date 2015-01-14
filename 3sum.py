# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

def threeSum(num):
    result = []
    num.sort()
    n_start = -1
    p_start = len(num)
    print num
    for i in range(len(num)):
        if num[i] < 0:
            n_start = i
        if p_start == len(num) and num[i] > 0:
            p_start = i

    # print n_start,p_start

    if (n_start == -1 and p_start - n_start > 3) or (p_start == len(num) and p_start - n_start > 3):
        return [[0,0,0]]
    elif len(num) < 3 or n_start == -1 or p_start == len(num):
        return result

    for i in range(n_start+1):
        for j in range(p_start, len(num)):
            remainder = 0 - num[i] - num[j]
            exists = False

            if remainder <= num[n_start]:
                exists = remainder in num[0:i] or remainder in num[i+1:n_start+1]
            elif remainder > num[n_start] and remainder <= num[p_start]:
                exists = remainder in num[n_start+1:p_start+1]
            elif remainder > num[p_start]:
                exists = remainder in num[p_start+1:j] or remainder in num[j+1:]


            if exists:
                triplet = sorted([num[i], num[j], remainder])
                if triplet not in result:
                    result.append(triplet)
    return result

S =  [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
S1 = [-1, -1 -1, 0, 2]
S2 = [-1,0,1,2,3]
S3 = [0,0,0,0,0,]
S4 = [-1,-1,-1,-1]
S5 = [2,2,2,2,2]
print threeSum(S)

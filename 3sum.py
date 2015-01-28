# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Soution1 - too slow

# def threeSum(num):
#     result = []
#     num.sort()
#     n_start = -1
#     p_start = len(num)
#     print num
#     for i in range(len(num)):
#         if num[i] < 0:
#             n_start = i
#         if p_start == len(num) and num[i] > 0:
#             p_start = i
#
#     # print n_start,p_start
#
#     if (n_start == -1 and p_start - n_start > 3) or (p_start == len(num) and p_start - n_start > 3):
#         return [[0,0,0]]
#     elif len(num) < 3 or n_start == -1 or p_start == len(num):
#         return result
#
#     for i in range(n_start+1):
#         for j in range(p_start, len(num)):
#             remainder = 0 - num[i] - num[j]
#             exists = False
#
#             if remainder <= num[n_start]:
#                 exists = remainder in num[0:i] or remainder in num[i+1:n_start+1]
#             elif remainder > num[n_start] and remainder <= num[p_start]:
#                 exists = remainder in num[n_start+1:p_start+1]
#             elif remainder > num[p_start]:
#                 exists = remainder in num[p_start+1:j] or remainder in num[j+1:]
#
#
#             if exists:
#                 triplet = sorted([num[i], num[j], remainder])
#                 if triplet not in result:
#                     result.append(triplet)
#     return result
#
# S =  [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
# S1 = [-1, -1 -1, 0, 2]
# S2 = [-1,0,1,2,3]
# S3 = [0,0,0,0,0,]
# S4 = [-1,-1,-1,-1]
# S5 = [2,2,2,2,2]


# Solution 2 - still too slow
#
# def threeSum(num):
#     result = set([])
#     if len(num) < 3:
#         return []
#     else:
#         for i in range(len(num)-2):
#             for j in range(i+1,len(num)-1):
#                 for k in range(j+1, len(num)):
#                     if not sum([num[i], num[j], num[k]]):
#                         result.add(tuple(sorted([num[i], num[j], num[k]])))
#
#         return list(result)

# Solution 3 - still too slow
# def threeSum(num):
#     two_sums = dict()
#     result = set([])
#     if len(num) < 3:
#         return []
#     else:
#         for i in range(len(num)-1):
#             for j in range(i+1, len(num)-1):
#                 if two_sums.has_key(num[i] + num[j]):
#                     two_sums[num[i] + num[j]].append((i,j))
#                 else:
#                     two_sums[num[i]+num[j]] = [(i,j)]
#
#         for i,n in enumerate(num):
#             remainder = 0 - n
#             if two_sums.has_key(remainder):
#                 for x,y in filter(lambda (x,y):x!=i and y!=i, two_sums[remainder]):
#                     result.add(tuple(sorted([n,num[x],num[y]])))
#
#         return list(result)

def threeSum(num):
    num.sort()
    returnList = []

    if len(num) < 3:
        return returnList
    else:
        for i in range(len(num)-2):
            if i > 0 and num[i] == num[i-1]:
                continue # This num is equal to previous num, skip it
            else:
                num1 = num[i]
                remainder = 0 - num1 # This is what we need to find
                begin = i + 1
                end = len(num) - 1
                while begin < end:
                    num2 = num[begin]
                    num3 = num[end]
                    if num2 + num3 == remainder:    # Successfully find a triplet
                        returnList.append([num1, num2,num3])
                        # Begin and end both go to the next different number
                        begin += 1
                        while begin < end and num[begin] == num[begin-1]:
                            begin += 1

                        end -= 1
                        while begin < end and num[end] == num[end+1]:
                            end -= 1

                    elif num2 + num3 < remainder:
                        # Begin go to next different number
                        begin += 1
                        while begin < end and num[begin] == num[begin-1]:
                            begin += 1

                    elif num2 + num3 > remainder:
                        # End go to next different number
                        end -= 1
                        while begin < end and num[end] == num[end+1]:
                            end -= 1


        return returnList


# S = [-1, 0, 1, 2, -1, -4]
print threeSum(S)

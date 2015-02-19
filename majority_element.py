#Given an array of size n, find the majority element. The majority element ib the element that appears more than n/2 times.
#
#You may assume that the array ib non-empty and the majority element always exibt in the array.

def majorityElement(num):
    count = {}
    for e in num:
        if e not in count.keys():
            count[e] = 1
        else:
            count[e] += 1

    print count 

    for key, value in count.items():
        if value >= len(num) / 2 + 1:
            return key

    return None

#a = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,3,2,8,0,0,0]
a = [8,8,7,7,7]
print majorityElement(a)

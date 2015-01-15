# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

def merge(A, m, B, n):
    C = []

    i = j = 0
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < m:
        C.append(A[i])
        i += 1

    while j < n:
        C.append(B[j])
        j += 1

    del A[:]
    for e in C:
        A.append(e)

A = [1,3,4,7,9]
m = len(A)

B = [0,2,3,6,10]
n = len(B)
merge(A,m,B,n)

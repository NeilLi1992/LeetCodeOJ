def removeDuplicates(A):
    if not A:   return len(A)

    index = 0
    while index < len(A) - 1:
        print index, len(A)-1
        while A.count(A[index]) > 1:
            del A[index]
        index += 1
    return len(A)

print removeDuplicates([1,1])

def removeElement(A, elem):
    while elem in A:
        A.remove(elem)
    return len(A)

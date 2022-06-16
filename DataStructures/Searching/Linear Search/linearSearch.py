# Searching


def linearSearch(A,key):
    n = len(A)-1
    index = 0
    while index <= n:
        if A[index] == key:
            return index
        index += 1
    return -1

A = [1,2,3,4,5,6,7,8,9]

print(linearSearch(A,8))
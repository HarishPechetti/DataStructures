# Searching using for loop linear search


def linearSearch_for(A,key):

    for i in range(len(A)):
        if A[i]==key:
            return i
     
    return -1
    

A = [1,2,3,4,5,6,7,8,9]

print(linearSearch_for(A,9))
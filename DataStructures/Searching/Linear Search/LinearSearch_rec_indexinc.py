# Linear Searching using recursion


def linearSearch_rec(A,key,index=0):
    if index>=len(A):
        return -1
    elif A[index]==key:
        return index
    else:
        return linearSearch_rec(A,key,index+1)
    

A = [1,2,3,4,5,6,7,8,9]

print(linearSearch_rec(A,10))
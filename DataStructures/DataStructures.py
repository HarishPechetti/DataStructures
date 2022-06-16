# Linear Searching using recursion decrement using length


def linearSearch_rec_indexdec(A,key,n):
    
    index = n-1
    if index<0:
        return -1
    elif A[index]==key:
        return index
    else:
        return linearSearch_rec(A,key,n-1)
    

A = [1,2,3,4,5,6,7,8,9]

print(linearSearch_rec(A,1,len(A)))
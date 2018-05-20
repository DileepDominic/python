def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if(A[j] < A[j-1]):
                swap(A,j,j-1)
                             
A = [ 4,5,7,1,4,2,8,90,87]

bubblesort(A)
print(A)

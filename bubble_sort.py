def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if(A[j] < A[j-1]):
                swap(A,j,j-1)
                             
A = [ 3,8,2,5,4,9,10,1]

bubblesort(A)
print(A)

"""Sample iteration

3	8	2	5	4	9	10	1
3	8	2	5	4	9	1	10
3	8	2	5	4	1	9	10
3	8	2	5	1	4	9	10
3	8	2	1	5	4	9	10
3	8	1	2	5	4	9	10
3	1	8	1	5	4	9	10
1	3	2	1	5	4	9	10

"""

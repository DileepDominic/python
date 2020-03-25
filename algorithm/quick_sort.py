def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def partition(A,start,end):
    i = start + 1;      
    pivot = A[start]

    for j in range(i,end):
        if(A[j] < pivot):    
            swap(A,i,j)
            i = i + 1
    swap(A,start,i-1)
    return i-1

def quicksort(A,start,end):
    if(start < end):
        pivot =partition(A,start,end)
        quicksort(A,start,pivot-1)
        quicksort(A,pivot+1,end)
        
A = [3,8,8,2,5,4,9,10,1]
quicksort(A,0,len(A))
print(A)

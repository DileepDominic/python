import bisect

def index_bisect(a,x):
    i = bisect.bisect_left(a,x)
    if i!= len(a) and a[i] == x:
        return i
    raise ValueError

collection = [10,2,3,4,5,6]

v = index_bisect(collection,10)
print(v)


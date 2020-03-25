
#this needs ordered list
def binarySearch(input_list,value_to_find):

    min = 0
    max = len(input_list) - 1

    while (min < max):
        mid = (min + max)//2

        if input_list[mid] > value_to_find:
            max = mid - 1
        elif input_list[mid] < value_to_find:
            min = mid + 1
        else:
            return mid
        
    return -1

input_list = [10,20,30,40,50,60,70,80,90,100]
print(binarySearch(input_list,100))



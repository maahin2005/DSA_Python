arr = [13,2,4,5,1]
target = 6

def findTarget(target,arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            sum_ = arr[i] + arr[j]
            if sum_ == target:
                print(i,j)

    return -1
findTarget(target,arr)
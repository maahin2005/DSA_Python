def checkPair(arr, k):
    arr.sort()
    N = len(arr)
    l = 0
    r = N - 1

    while l < r:
        sum_ = arr[l] + arr[r]
        if sum_ == k:
            return True
        elif sum_ < k:
            l+=1
        else:
            r-=1
    
    return False

arr = [1,4,3,6,11,9,5]
k=16
print(checkPair(arr, k))
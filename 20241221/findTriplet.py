def checkTriplet(arr,k):
    N = len(arr)
    i = 0
    while i < N - 2:
        l = i + 1
        r = N - 1

        while l < r:
            sum_ = arr[i] + arr[l] + arr[r]

            if sum_ == k:
                return True
            elif sum_ < k:
                l+=1
            else:
                r-=1
        i += 1
    
    return False

arr = [1,4,3,6,11,9,5]
k=25
print(checkTriplet(arr,k))
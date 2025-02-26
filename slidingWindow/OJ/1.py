# SUM OF SUB_ARRAY

# BRUTE FORCE

arr = [1,2,1,2,3,4]
k = 90

def targetK(arr, k):
    sum_ = 0

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum_+= arr[j]
            if sum_ == k:
                return True
    
    return False


# optimal

def slidingWindow(arr,k):
    s = 0
    start = 0
    end = 0

    while end < len(arr):
        s += arr[end]

        if start < len(arr) and s > k:
            s -= arr[start]
            start += 1
        if s == k:
            return True
        end += 1
    return False

print(slidingWindow(arr,k))
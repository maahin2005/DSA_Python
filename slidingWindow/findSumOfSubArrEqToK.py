def findSumOfSubArrEqToK(arr,k):
    N = len(arr)

    high = 0
    low = 0
    windowSum = 0
    while low < N:
        while high < N and windowSum < k:
            windowSum += arr[high]
            high += 1
        
        if windowSum == k:
            sizeOfWindow = high - low

            return sizeOfWindow, arr[low:high]
        
        windowSum = windowSum - arr[low]
        low += 1
    
    return False
        
arr = [2,4,20,3,10,6]
k=13
print(findSumOfSubArrEqToK(arr,k))
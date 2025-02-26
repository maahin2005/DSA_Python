arr = [2,4,1,4,6]
k = 3

# Brute force approach for finding fix sized sliding window
def maxSum(arr, k):
    maxSum = 0

    for i in range(len(arr)-k+1):
        s = 0
        for j in range(i, i + k):
            s += arr[j]
        maxSum = max(maxSum, s)
    
    return maxSum

result = maxSum(arr, k)
print(result)


windowSum = sum(arr[:k])
maxSum = windowSum

for i in range(len(arr)-k):
    windowSum = (windowSum - arr[i]) + arr[i + k]
    maxSum = max(maxSum, windowSum)

print(maxSum)
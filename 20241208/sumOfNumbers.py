def sumOfNumber(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    return sum

arr = [1,2,3,4,5]
print(sumOfNumber(arr))
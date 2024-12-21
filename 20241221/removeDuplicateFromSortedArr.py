def removeDuplicateFromSortedArr(arr):
    j = 0
    n = len(arr)
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j+=1
    
    arr[j] = arr[n-1]

    return arr[0:j]

arr = [1,1,1,2,2,3,3,3,4,5,5]
print(removeDuplicateFromSortedArr(arr))
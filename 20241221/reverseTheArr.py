def revTheArr(arr):
    N = len(arr)
    l = 0
    r = N - 1

    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

        l += 1
        r -= 1

arr = [0,1,2,3,4,5,6,7,8,9]
revTheArr(arr)
print(arr)
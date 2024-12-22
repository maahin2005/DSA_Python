def sepEvenOdd(arr):
    N = len(arr)
    l = 0
    r = N - 1

    while l < r:
        isEven = arr[l] % 2 == 0
        isOdd = arr[r] % 2 != 0
        
        if not isEven and not isOdd:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l+= 1
            r -= 1
        elif isEven:
            l+=1
        elif isOdd:
            r-=1
        else:
            l+= 1
            r -= 1

arr=[13,1,12,14,15,16,17,18,19,20,21,5,0]
sepEvenOdd(arr)
print(arr)

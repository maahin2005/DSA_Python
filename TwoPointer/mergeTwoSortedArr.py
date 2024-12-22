def mergeTwoSortedArr(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    tempArr = [0 for i in range(n1+n2)]

    l = 0
    r = 0
    p = 0

    while l < n1 and r < n2:
        if arr1[l] < arr2[r]:
            tempArr[p] = arr1[l]
            l+=1
        else:
            tempArr[p] = arr2[r]
            r+=1
        p+=1

    while l < n1:
        tempArr[p] = arr1[l]
        l+=1
        p+=1
    
    while r < n2:
        tempArr[p] = arr2[r]
        r+=1
        p+=1
    
    
    return tempArr

arr1 = [1,3,5,10,12]
arr2 = [2,4,6,11,20,22,33]

print(mergeTwoSortedArr(arr1, arr2))
def searchInsert(nums,target):
    N = len(nums)

    l = 0
    r = N - 1

    if target > nums[r]:
        return N
    
    if target < nums[l]:
        return 0

    while l <= r:
        
        mid = (l + r) // 2
        
        if nums[mid] < target and  mid < N - 1:
            if (nums[mid + 1] > target):
                return mid + 1
        
        if nums[mid] > target and nums[mid - 1] < target:
            return mid

        if nums[mid] == target:
            return mid
        else:
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))
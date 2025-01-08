def distinctAverages(nums):
    nums.sort()
    N = len(nums)
    i = 0
    j = N - 1
    distincts = set() 

    while i < j:        
        avg_ = (nums[i] + nums[j]) / 2
        distincts.add(avg_)

        i += 1
        j -= 1

    return len(distincts)

nums = [1,100]
print(distinctAverages(nums))
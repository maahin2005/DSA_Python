# Basic Problems (15 minutes)

# Problem 1: Two Sum (Sorted Array)

# Given a sorted array, find two numbers that add up to a target.

# Approach:

# Use two pointers: one at the start (left), one at the end (right).

# Move pointers towards each other based on the sum compared to the target.

def twoSum(arr, target):
    N = len(arr)
    start = 0
    end = N - 1

    while start < end:
        sum_= arr[start] + arr[end]

        if sum_ == target:
            return [start, end]
        elif sum_ > target:
            end-=1
        else:
            start+=1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5

result = twoSum(arr, target)

print(result)
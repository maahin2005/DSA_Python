# Problem Remove Duplicates from Sorted Array

# Given a sorted array, remove duplicates in-place and return the new length.

# BRUTE_FORCE
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def remove_duplicates(arr):

    i = 1
    while i < len(arr):
        if arr[i] and arr[i] == arr[i-1]:
            del arr[i]
        else:
            i+=1
    return len(arr)

arr = [1, 1, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(arr)
print(result)

# Better



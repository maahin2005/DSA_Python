def longestCommonPrefix(arr):
    N = len(arr)
    arr.sort()
    length_ = min(len(arr[0]), len(arr[N - 1]))
    str_1 = arr[0]
    str_2 = arr[N - 1]
    prefix_ = ""
    for i in range(length_):
        if str_2[i] == str_1[i]:
            prefix_ += str_1[i]
        else:
            break
        
    return prefix_
        

arr = ["c","acc","ccc"] 
print(longestCommonPrefix(arr))
print(arr)

# def longestCommonPrefix(self, strs):
#    longest_pre = []
 
#    if strs and len(strs) > 0:
#       strs = sorted(strs) 
#       first, last = strs[0], strs[-1] 
#       for i in range(len(first)):
#          if len(last) > i and last[i] == first[i]:
#             longest_pre.append(last[i])
#          else:
#             return “”.join(longest_pre)
#    return “”.join(longest_pre)
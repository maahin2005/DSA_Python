# def sepZeroOneBrute(arr):
#     N = len(arr)
#     zeros = []
#     ones = []
#     for i in range(N):
#         if arr[i] == 0:
#             zeros.append(arr[i])
#         else:
#             ones.append(arr[i])
    
#     return (zeros + ones)

arr = [1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0]
# print(sepZeroOneBrute(arr))

def sepZeroOne(arr):
    N = len(arr)

    l = 0
    r = N - 1

    while l < r:
        if arr[l] == 1 and arr[r] == 0:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
        elif arr[l] == 1 and arr[r] == 1:
            r -= 1
        elif arr[l] == 0 and arr[r] == 0:
            l += 1
        else:
            l+= 1
            r-=1
sepZeroOne(arr)
print(arr)
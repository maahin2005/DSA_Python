def findSubArr(arr):
   N = len(arr)

   for i in range(N):
      for j in range(i+1,N+1):
        print(arr[i:j])

arr = [1,2,3]

findSubArr(arr)

def sumOfSubArr(arr):
   N = len(arr)

   for i in range(N):
      for j in range(i+1,N+1):
         sum_ = sum(arr[i:j])
         print(sum_)

sumOfSubArr(arr)
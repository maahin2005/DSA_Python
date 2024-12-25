def sumOfTwoNum(array, target):
    num_disc = {}

    for i, num in enumerate(array):
        complement = target - num
        
        if complement in num_disc:

            return [num_disc[complement], i]

        num_disc[num] = i
    return False

array = [3,2,4]
target = 6
print(sumOfTwoNum(array, target))

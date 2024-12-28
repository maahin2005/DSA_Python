def divideAndSum(num,k):
    sum_=0
    for i in range(num):
        if i % k == 0:
            sum_ += i

    return sum_

try:
    number = int(input("Enter the Number: "))
    k = int(input("Enter the Divider Number: "))

    print(f"The sum of between 1 to {number} is {divideAndSum(number, k)}, which are devided by {k}")
except Exception as e:
    print(f"Error: {e}")
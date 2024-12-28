num = input("Enter any non negative number: ")

if(not num.isnumeric()):
    print("Please enter a number")

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(num)
print(factorial(number))
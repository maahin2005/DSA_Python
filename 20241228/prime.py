def isPrime(num):
    if num <= 0:
        return "Please Enter valid Number"

    for i in range(2,num):
        if num % i == 0:
            return "It is not a prime number"
    
    return "It is a prime number"

num = 15
print(isPrime(num))
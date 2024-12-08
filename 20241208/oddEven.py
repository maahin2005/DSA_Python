def oddEven(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

num = int(input("Enter Number: "))
oddEven(num)
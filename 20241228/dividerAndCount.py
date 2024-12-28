def divideAndCount(start,end,divider):
    count = 0
    for i in range(start, end+1):
        if i % divider == 0:
            count += 1

    return count

try:
    start = int(input("Enter the start: "))
    end = int(input("Enter the end: "))
    divider = int(input("Enter the divider: "))
    print(f"The total number of between {start} to {end} is {divideAndCount(start,end,divider)} which is divided by {divider}")
except Exception as e:
    print("Error: " + e)
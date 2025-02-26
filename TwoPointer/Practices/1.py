string = "asbfijjjkoi"

# Brute force
def brute_force():

    start = 0
    end = 1
    vowels = "aeiou"
    maxLength = 0

    while end < len(string):
        st = ""
        if string[start] not in vowels:
            st += string[start]
        end = start + 1
        while end < len(string) and string[end] not in vowels:
            st += string[end]
            end += 1
        start+=1
        maxLength = max(maxLength, len(st))

    print(maxLength)

# Optimal Approach

def optimize():
    start = 0
    maxLength = 0
    vowels = "aeiou"
    for end in range(len(string)):
        if string[end] in vowels:
            start = end + 1
        else:
            maxLength = max(maxLength, (end - start) + 1)
    
    print(maxLength)

brute_force()
optimize()
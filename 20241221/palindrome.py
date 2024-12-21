def palindrome(string):
    N = len(string)
    l = 0
    r = N - 1

    while l < r:
        if string[l] != string[r]:
            return False
        
        l += 1
        r -= 1
    
    return True

string = "aaba"
print(palindrome(string))
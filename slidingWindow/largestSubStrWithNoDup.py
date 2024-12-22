def largestSubStrWithNoDup(string):
    N = len(string)

    obj = {}

    start = 0
    i = 0
    maxLength= 0
    

    while i<N:
        if string[i] in obj:
           start = max(start, obj[string[i]]+1)
        
        obj[string[i]] = i
        maxLength = max(maxLength, (i - start) + 1)
        i += 1
    print(maxLength)

string = "abbcdeabb"
largestSubStrWithNoDup(string)

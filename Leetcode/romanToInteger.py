def romanToInteger(s):
    N = len(s)

    hx = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    sum_ = 0
    i = 0
    while i < (N-1):
        if hx[s[i]] < hx[s[i + 1]]:
            tempSum = hx[s[i + 1]] - hx[s[i]]
            sum_ += tempSum
            i += 2
        else:
            sum_ += hx[s[i]]
            i+=1
    
    if i == N-1:
        sum_ += hx[s[i]]
        
    return sum_


s= input("Enter Roman Number: ")
print(romanToInteger(s))
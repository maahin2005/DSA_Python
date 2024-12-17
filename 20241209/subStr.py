def findSubStr(str):
    N = len(str)

    for i in range(N):
        for j in range(i+1,N+1):
            print(str[i:j])

string = "abbddefe"
# findSubStr(string)

def reverseTheStr(string):
    N = len(string)
    result = ""
    for i in range(N-1, -1, -1):
        result += string[i]
    
    return result

def checkPallindrome(string):
    N = len(string)

    pallindromes = []

    for i in range(N):
        for j in range(i+1,N+1):
            temp = string[i:j]

            rev = reverseTheStr(temp)
            if temp == rev and len(temp) > 1:
                pallindromes.insert(temp)
                print("Pallindrome is exist: " + temp)
    
    # for i in range(len(pallindromes)):
    #     maxL = len(i)
    #     curr = i

    #     if maxL < len(i):
    #         maxL = len(i)
            

    
checkPallindrome(string)
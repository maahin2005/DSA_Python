def reverseTheStr(string):
    n = len(string)- 1

    newStr = ""

    for i in range(n, -1,-1):
        newStr += string[i]
    
    return newStr

string = input("Enter any Name: ").replace(" ", "")
print(reverseTheStr(string))


    
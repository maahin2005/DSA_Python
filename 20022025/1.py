s = "01101"
s = "11"

N = len(s)
sum_= int(s[0])
for i in range(1,N):
    if s[i] == s[i-1]:
        sum_-=int(s[i])
    else:
        sum_+=int(s[i])

print(sum_)

# find the continues maxLength substr of consonants

s="aa"
maxLength=0
ans = ""
st = 0
for i in range(len(s)):
    if s[i] in "aeiou":
        st = i + 1
    else:
        maxLength=max(maxLength, (i - st) + 1)
        str_ = s[st:i+1]
        if len(str_) == maxLength:
            ans = str_
    

print(maxLength, ans)


def lengthOfLongestSubstring(s):
    N = len(s)
    max_length = 0
    l = 0
    hx = {}

    for r in range(N):
        if s[r] in hx and hx[s[r]] >= l:
            # Move the left pointer to the right of the last occurrence
            l = hx[s[r]] + 1
        # Update the hash map with the current character's index
        hx[s[r]] = r
        # Calculate the maximum length
        max_length = max(max_length, r - l + 1)

    return max_length

s = "pwwkew"
print(lengthOfLongestSubstring(s))

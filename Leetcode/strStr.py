def strStr(haystack: str, needle: str) -> int:
    # Get the lengths of haystack and needle
    haystack_len = len(haystack)
    needle_len = len(needle)
    
    # If needle is empty, return 0
    if needle_len == 0:
        return 0
    
    # Iterate through haystack
    for i in range(haystack_len - needle_len + 1):
        # Check if the substring matches needle
        if haystack[i:i + needle_len] == needle:
            return i
    
    # If no match is found, return -1
    return -1

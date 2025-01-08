def countPrefixSuffixPairs(words):
    def isPrefixAndSuffix(prefix, suffix):
        # Check if `prefix` is a prefix of `suffix` and a suffix of `suffix`
        prefix_len = len(prefix)
        suffix_len = len(suffix)
        if prefix_len > suffix_len:
            return False
        return suffix.startswith(prefix) and suffix.endswith(prefix)
    
    count = 0
    N = len(words)
    
    # Compare every pair of words
    for i in range(N):
        for j in range(i + 1, N):
            if isPrefixAndSuffix(words[i], words[j]):
                count += 1
    
    return count

words = ["a","abb"]
print(countPrefixSuffixPairs(words))
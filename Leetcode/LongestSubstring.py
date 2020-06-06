def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    this_dict = {}
    max_length = start = 0

    for i in range(len(s)):
        if s[i] in this_dict and start <= this_dict[s[i]]:
            start = this_dict[s[i]] + 1
        else:
            max_length = max(max_length, i-start+1)
        this_dict[s[i]] = i
    return max_length

print(lengthOfLongestSubstring("tmmzuxt"))
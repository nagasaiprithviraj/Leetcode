import collections
def firstUniqChar(s):
    this_dict = {}
    for i in range(len(s)):
        if s[i] not in this_dict:
            this_dict[s[i]] = s.count(s[i])
    print(this_dict)
    # temp = -1
    for x in this_dict:
        # temp += 1
        if this_dict[x] == 1:
            return s.index(x)
        else:
            continue
    return -1

def firstUniqChar_1(s):
    count = collections.Counter(s)
    print(count)
    a = enumerate(s)
    print(list(a))
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


if __name__ == '__main__':
    # print(firstUniqChar("leetcode"))
    # print(firstUniqChar("dddccdbba"))
    print(firstUniqChar_1("loveleetcode"))
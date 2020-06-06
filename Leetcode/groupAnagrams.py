def groupAnagrams(strs):
    this_dict = {}
    for s in strs:
        c = "".join(sorted(s))
        if c not in this_dict:
            this_dict[c] = [s]
        else:
            this_dict[c].append(s)
    x = sorted(this_dict, key=lambda k: len(this_dict[k]), reverse=False)
    Res = []
    for i in x:
        Res.append(this_dict[i])
    return Res

if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
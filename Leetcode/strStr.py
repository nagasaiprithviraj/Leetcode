def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif needle in haystack:
        return haystack.index(needle)
    else:
        return -1

if __name__ == '__main__':
    # strStr("Hello", "ll")
    print(strStr("Hello", "ll"))
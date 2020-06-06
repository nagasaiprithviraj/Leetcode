def myAtoi(s):
    s = s.strip()

    # For empty string return 0
    if not s:
        return 0

    # For positive and negative values, other conditions
    negative = False
    ans = 0

    if s[0] == "-":
        negative = True
    elif s[0] == "+":
        negative = False
    elif not s[0].isnumeric(): # for string values starting with words
        return 0
    else:
        ans = ord(s[0]) - ord("0")

    for i in range(1, len(s)):
        if s[i].isnumeric():
            ans = (ans*10) + (ord(s[i]) - ord("0"))
            if not negative and ans >= 2147483647:
                return 2147483648
            if negative and ans >= 2147483648:
                return -2147483648
        else:
            break

    if not negative:
        return ans
    else:
        return -ans


class Solution:
    def __init__(self):
        self.str = str


if __name__ == '__main__':
    # print(myAtoi("    -42"))
    print(myAtoi("3.123456"))

    # print(myAtoi("4193 with words"))
    # print(myAtoi("-91283472332"))
    # print(myAtoi("     "))
    # print(myAtoi("with words 4193"))
    # print(myAtoi(" with words 4193 "))




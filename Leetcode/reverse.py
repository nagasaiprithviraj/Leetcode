def reverse(x):
    x = str(x)
    negative = True
    Res = ""
    if not x:
        return 0

    if x[0] == '-':
        negative = True
        x = x.replace('-', '')
    else:
        negative = False
    for i in reversed(x):
        Res += i
    Res = int(Res)
    if not negative and ((2**31)-1) >= Res >= -(2 ** 31):
        return Res
    elif negative and ((2**31)-1) >= Res >= -(2 ** 31):
        return -Res
    else:
        return 0


if __name__ == '__main__':
    print(reverse(-2147483648))
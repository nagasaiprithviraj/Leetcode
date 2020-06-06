def IntToRoman(num):
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    return thousands[num//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones [num%10]


if __name__ == '__main__':
    # print(IntToRoman(43))
    # IntToRoman(43)
    print(IntToRoman(3459))

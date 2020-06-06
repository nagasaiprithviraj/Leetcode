class Solution:
    def RomanToInt(self, roman):
        self.roman = roman
        this_dict = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000,
                     "IV": 4,
                     "XL": 40,
                     "CD": 400,
                     "IX": 9,
                     "XC": 90,
                     "CM": 900
                     }
        temp = 0
        y = -1
        for i in range(len(roman)):
            a = roman[i]
            if roman[i:i + 2] in this_dict and (i<(len(roman)-1)):
                temp += this_dict[roman[i:i + 2]]
                y = i+1
            elif i == y:
                continue
            else:
                temp += this_dict[roman[i]]
        return temp


if __name__ == '__main__':
    print(Solution().RomanToInt("MMMCDLIX"))
    print(Solution().RomanToInt("LVIII"))

    # print(RomanToInt("III"))


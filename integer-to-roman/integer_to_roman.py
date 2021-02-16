class Solution_Optimal(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hud = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tud = ["", "M", "MM", "MMM"]
        return tud[num/1000%10] + hud[num/100%10] + ten[num/10%10] + one[num%10]



class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        def get_one(decimals):
            if decimals == 1:
                return 'I'
            elif decimals == 10:
                return 'X'
            elif decimals == 100:
                return 'C'
            elif decimals == 1000:
                return 'M'

        def get_five(decimals):
            if decimals == 1:
                return 'V'
            elif decimals == 10:
                return 'L'
            elif decimals == 100:
                return 'D'

        def get_roman(num, decimal):
            result = ""
            if num == 0:
                pass
            elif num < 4:
                # 1, 2, 3
                for x in range(num):
                    result += get_one(decimal)
            elif num == 4:
                # 4
                result = get_one(decimal) + get_five(decimal)
            elif num < 9:
                # 5, 6, 7, 8
                result = get_five(decimal)
                for x in range(num - 5):
                    result += get_one(decimal)
            elif num == 9:
                # 9
                result = get_one(decimal) + get_one(decimal*10)
            return result

        result = ""
        for i, char in enumerate(str(num)):
            print("converting: " + char)
            decimal = 10 ** (len(str(num)) - i - 1)
            print("decimal: " + str(decimal))
            char_in_roman = get_roman(int(char),decimal)
            print("current decimal in roman: " + char_in_roman)
            result += char_in_roman

        return result



def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print("******************************************************************************")
            line = next(lines)
            num = stringToInt(line)
            print("number to convert: " + str(num))

            ret = Solution().intToRoman(num)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
class Solution_Optimal(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """

        INT_MIN = -2**31
        INT_MAX = 2**31-1
        string = string.strip()
        if string == None or len(string) == 0:
            return 0
        if string[0] != '-' and string[0] != '+' and not string[0].isdigit():
            return 0
        res = 0
        tmp = string[0]
        for i in range(1, len(string)):
            if not string[i].isdigit():
                break
            tmp += string[i]
        if tmp == '+' or tmp == '-':
            return 0
        carry = 1
        for i in range(len(tmp)-1, 0, -1):
            res += int(tmp[i]) * carry
            carry *= 10
        if tmp[0] == '-':
            res = -res
        if tmp[0].isdigit():
            res += int(tmp[0]) * carry
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        i = 0
        while i<len(s) and s[i] == ' ':
            i += 1
            # print("skipping empty space. i=" + str(i))

        # no integer found
        if i == len(s):
            # print("no integer found. returning zero")
            return 0

        # check for minus or plus sign
        negative = False
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1

        # print("number start at index: " + str(i))

        # check for signal without number
        if len(s) == i:
            return 0

        if not s[i].isdigit():
            # print("not a digit. returning zero")
            return 0

        number_string = ""
        for char_index in range(i,len(s)):
            if s[char_index].isdigit():
                # print(s[char_index] + " is digit")
                number_string += s[char_index]
            else:
                break
            # if len(number_string) == 11:
            #     # print("number getting too big. stopping here")
            #     break

        # print("abs number string: " + number_string)

        if negative:
            return max(-2**31,int(number_string)*-1)
        else:
            return min(2**31-1,int(number_string))



def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print("**************************** start *******************************")
            line = next(lines)
            str = stringToString(line)
            print("string to be converted: " + str)
            ret = Solution().myAtoi(str)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
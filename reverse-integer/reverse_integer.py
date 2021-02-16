class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = False
        if str(x)[0] == '-':
            negative = True

        reversed_int = int(str(abs(x))[::-1])
        if negative:
            reversed_int = reversed_int * -1

        # print("reversed int: " + str(reversed_int))
        if reversed_int > (2**31-1) or reversed_int < (-2**31):
            return 0
        else:
            return reversed_int


def stringToInt(input):
    return int(input)

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
            x = stringToInt(line)
            print("integer to be converted: " + str(x))
            ret = Solution().reverse(x)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2

        result = 0
        prev1 = 2
        prev2 = 1
        for i in range(3,n+1):
            result = prev1 + prev2
            prev2 = prev1
            prev1 = result

        return result


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
            print("********************** start ************************")
            line = next(lines)
            n = stringToInt(line)
            print("steps: " + str(n))
            ret = Solution().climbStairs(n)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
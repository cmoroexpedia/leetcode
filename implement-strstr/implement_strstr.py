class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        res = -1
        # bruteforce solution
        for i in range(len(haystack)):
            # print("looking at char: " + str(haystack[i]))
            # compare current char with first char of needle
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    # print("setting res to: " + str(i))
                    res = i
                    break
        return res



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
            print("********************** start ************************")
            line = next(lines)
            haystack = stringToString(line)
            print("Haystack: " + haystack)
            line = next(lines)
            needle = stringToString(line)
            print("Needle: " + needle)

            ret = Solution().strStr(haystack, needle)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
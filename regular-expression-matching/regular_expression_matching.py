
class Solution(object):
    def isMatch(self, text, pattern):

        # print("---> function isMatch called with " + str(text) + " , " + str(pattern))

        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])



def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)
            print("string: " + s)
            line = next(lines)
            p = stringToString(line)
            print("pattern: " + p)
            ret = Solution().isMatch(s, p)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

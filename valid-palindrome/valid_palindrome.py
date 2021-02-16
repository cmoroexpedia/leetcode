class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == None or s == "":
            return True

        left = 0
        right = len(s)-1
        # will iterate from edges inward

        ans = True
        while left < right:
            # print("checking s[{}]={}; s[right]={}: {}".format(left, s[left].lower(), right, s[right].lower()))
            #check for non-alphanumeric
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                # print("chars {} and {} match".format(s[left].lower(),s[right].lower()))
                ans = True
            else:
                ans = False
                break
            left += 1
            right -= 1
        return ans


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
            print("********************** start ************************")
            line = next(lines)
            s = stringToString(line)
            print(s)

            ret = Solution().isPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
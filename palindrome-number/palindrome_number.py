class Solution_Optimal(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        xx = x[::-1]
        return x == xx


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        output = False
        s = str(x)
        if s[0] == '-' or s[0]=='+':
            return False
        if len(s) == 1:
            return True

        if len(s) % 2 == 0:
            # even size
            middle = len(s)/2
            # print("middle (including): " + str(middle))
            left_index = middle -1
            right_index = middle
            while left_index>=0 and left_index<len(s):
                if s[left_index] == s[right_index]:
                    # print('s[left_index] == s[right_index] (' + s[left_index] + "==" + s[right_index] + ")")
                    output = True
                else:
                    output = False
                    break
                left_index -= 1
                right_index += 1

        else:
            # odd size
            middle = len(s)/2
            # print("middle (excluding): " + str(middle))
            left_index = middle -1
            right_index = middle +1
            while left_index>=0 and left_index<len(s):
                if s[left_index] == s[right_index]:
                    # print('s[left_index] == s[right_index] (' + s[left_index] + "==" + s[right_index] + ")")
                    output = True
                else:
                    output = False
                    break
                left_index -= 1
                right_index += 1

        return output


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
            print("**************************** start *******************************")
            line = next(lines)
            x = stringToInt(line)
            print("integer to be converted: " + str(x))

            ret = Solution().isPalindrome(x)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
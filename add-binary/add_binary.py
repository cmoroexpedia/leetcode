class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # initialize pointers to tail of number
        ptrA= len(a) - 1
        ptrB = len(b) - 1
        currA = a[ptrA]
        currB = b[ptrB]
        carry = 0
        sum = 0
        ans = ""

        while currA or currB or carry:
            # print "************************"
            # print "currA: {}".format(currA)
            # print "currB: {}".format(currB)
            # print "carry: {}".format(carry)
            if (currA is None) and (currB is None):
                sum = carry
            elif currA is None:
                sum = int(currB) + carry
            elif currB is None:
                sum = int(currA) + carry
            else:
                sum = int(currA) + int(currB) + carry

            # perform sum
            if sum == 3:
                sum = 1
                carry = 1
            elif sum == 2:
                sum = 0
                carry = 1
            elif sum < 2:
                carry = 0

            # print "sum: {}".format(sum)
            # print "carry: {}".format(carry)

            ptrA -= 1
            ptrB -= 1

            if ptrA < 0:
                currA = None
            else:
                currA = a[ptrA]

            if ptrB < 0:
                currB = None
            else:
                currB = b[ptrB]

            ans = str(sum) + ans

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
            print "********************** start ************************"
            line = lines.next()
            a = stringToString(line)
            print "a: {}".format(a)
            line = lines.next()
            b = stringToString(line)
            print "b: {}".format(b)

            ret = Solution().addBinary(a, b)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
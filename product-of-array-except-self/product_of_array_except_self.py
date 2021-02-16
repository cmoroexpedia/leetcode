import json

class Solution_Slow(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        # brute-force solution
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    # skip if current j is self
                    continue
                else:
                    product *= nums[j]
            ans.append(product)

        return ans

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        # initializing left and right arrays
        L = [1]*len(nums)
        R = [1]*len(nums)

        # will start populating the left array
        i = 1
        while i < len(nums):
            L[i] = L[i-1] * nums[i-1]
            i += 1
        # print(L)

        # will start populating the right array
        i = len(nums)-2
        while i >= 0:
            R[i] = R[i+1] * nums[i+1]
            i -= 1
        # print(R)

        # now we iterate over the elements and simply multiply L * R
        for i in range(len(nums)):
            product = L[i] * R[i]
            ans.append(product)

        return ans

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            nums = stringToIntegerList(line)
            print(nums)

            ret = Solution().productExceptSelf(nums)

            out = integerListToString(ret)
            print("out: " + str(out))
        except StopIteration:
            break

if __name__ == '__main__':
    main()
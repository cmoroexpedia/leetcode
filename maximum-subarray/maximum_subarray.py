import json

class Solution_Slow(object):
        def maxSubArray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """

            maxSum = sum(nums)

            # brute-force solution
            for i in range(len(nums)+1):
                for j in range (i+1, len(nums)+1):
                    subArray = nums[i:j]
                    # print(subArray)
                    sumSubArray = sum(subArray)
                    # print("sum: " + str(sumSubArray))
                    if sumSubArray > maxSum:
                        maxSum = sumSubArray

            return maxSum


class Solution_Better(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = float("-inf")

        for i in range(len(nums)):
            #this variable will always have the previous sum to avoid having to recalculate sum for same array
            curr_sum = nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            for j in range (i+1, len(nums)):
                curr_sum = curr_sum + nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum

# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = float("-inf")
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line)
            print("nums: " + str(nums))

            ret = Solution().maxSubArray(nums)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
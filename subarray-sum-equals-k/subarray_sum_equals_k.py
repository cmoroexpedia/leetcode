import json

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cum_sum = [nums[0]]
        # building a cumulative sum array
        for i in range(1,len(nums)):
            cum_sum.append(cum_sum[i-1]+nums[i])

        # print cum_sum

        ans = 0
        for i in range(len(nums)):
            # print nums[i]
            sum = nums[i]
            if sum == k:
                ans += 1

            j = i + 1
            while j < len(nums):
                # print nums[i:j+1]
                # print "i: {}, j: {}".format(i,j)
                if i == 0:
                    sum = cum_sum[j]
                else:
                    sum = cum_sum[j] - cum_sum[i-1]
                # print "current sum: {}".format(sum)
                if sum == k:
                    ans += 1
                j += 1


        return ans


class Solution_Slow(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # brute-force solution

        ans = 0

        for i in range(len(nums)):
            # print nums[i]
            sum = nums[i]
            if sum == k:
                ans += 1

            j = i + 1
            while j < len(nums):
                # print nums[i:j+1]
                sum += nums[j]
                if sum == k:
                    ans += 1
                j += 1

        return ans



def stringToIntegerList(input):
    return json.loads(input)

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
            print "**************************** start *******************************"
            line = lines.next()
            nums = stringToIntegerList(line)
            print "nums: {}".format(nums)
            line = lines.next()
            k = stringToInt(line)
            print "k: {}".format(k)

            ret = Solution().subarraySum(nums, k)

            out = intToString(ret)
            print "out: {}".format(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
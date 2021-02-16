import json

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # brute-force solution
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            elif nums[i] == target:
                return i
        return i+1




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
            print "********************** start ************************"
            line = lines.next()
            nums = stringToIntegerList(line)
            print "nums: " + str(nums)
            line = lines.next()
            target = stringToInt(line)
            print "target: " + str(target)

            ret = Solution().searchInsert(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
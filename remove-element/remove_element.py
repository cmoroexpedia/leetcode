import json

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # for elem in nums:
        #     print "looking at elem: " + str(elem)
        #     if elem == val:
        #         nums.remove(val)
        i = 0
        while i < len(nums):
            print "looking at elem at position: " + str(i) + "(" + str(nums[i]) + ")"
            if nums[i] == val:
                del nums[i]
                continue
            i += 1


def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

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
            print "********************** start ************************"
            line = lines.next()
            nums = stringToIntegerList(line)
            print "nums: " + str(nums)
            line = lines.next()
            val = stringToInt(line)
            print "val to be removed: " + str(val)

            ret = Solution().removeElement(nums, val)

            out = integerListToString(nums, len_of_list=ret)
            print "output: " + out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
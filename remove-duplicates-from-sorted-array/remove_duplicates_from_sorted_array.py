import json


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_size = len(nums) -1
        i = 0

        while i < nums_size:
            # print "i:" + str(i)
            # compare current number with next number
            if nums[i] == nums[i+1]:
                # if they are the same delete current number
                # print "deleting " + str(nums[i])
                del(nums[i])
                nums_size -= 1
            else:
                i += 1


def stringToIntegerList(input):
    return json.loads(input)

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
            print "original: " + str(line)
            nums = stringToIntegerList(line)

            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
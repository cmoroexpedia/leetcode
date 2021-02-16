import json


class Solution_Optimal(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for k, v in enumerate(nums):
            if target - v in dicts:
                return [dicts.get(target-v), k]
            dicts[v] = k


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sortedIndexes = self.getSortedIndex(nums)
        # print "sorted indexes: " + str(sortedIndexes)
        sortedNums = sorted(nums)
        # print "sorted nums: " + str(sortedNums)

        sum = 0
        # print "range: " + str(range(0,len(sortedNums)))
        for x in range(0,len(sortedNums)):
            # print "new iteration... x is now " + str(x)
            y = x + 1
            # print "y is now " + str(y)
            sum = sortedNums[x] + sortedNums[y]
            # print "current sum: " + str(sum)
            while (sum < target) and (y < len(sortedNums)-1):
                y += 1
                # print "y is now " + str(y)
                sum = sortedNums[x] + sortedNums[y]
                # print "current sum: " + str(sum)
            if sum == target:
                return sorted([sortedIndexes[x],sortedIndexes[y]])

        return "no match found"

    def getSortedIndex(self, myList):
        return [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            print "nums:" + str(nums)
            line = lines.next()
            target = stringToInt(line)
            print "target: " + str(target)

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print "result: " + out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
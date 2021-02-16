import json

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        # print "sorted intervals: " + str(intervals)

        ans = []
        i = 0
        while i < len(intervals):
            # print intervals[i]

            if i == len(intervals)-1:
                # I'm at last elem, so I'll just add to answer
                ans.append(intervals[i])
                i += 1
                continue

            if intervals[i][1] >= intervals[i+1][0]:
                # print "overlap with next!"
                # these two overlap, so I'll start merging
                min_left = min(intervals[i][0],intervals[i+1][0])
                max_right = max(intervals[i][1],intervals[i+1][1])

                i += 2
                # loop until intervals stop overlapping
                while (i < len(intervals)) and (intervals[i][0] <= max_right):
                    if intervals[i][0] < min_left:
                        min_left = intervals[i][0]
                    if intervals[i][1] > max_right:
                        max_right = intervals[i][1]
                    i += 1
                ans.append([min_left,max_right])

            else:
                # they don't overlap. Just add to answer and move to next
                ans.append(intervals[i])
                i += 1

        return ans

def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        print "********************** start ************************"
        try:
            line = lines.next()
            intervals = stringToInt2dArray(line)
            print intervals

            ret = Solution().merge(intervals)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
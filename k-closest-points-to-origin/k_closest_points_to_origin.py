import json
import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        ans = []
        distances = []

        # first, will go through list and calculate the distances
        for i in range(len(points)):
            # print(points[i])
            distance = math.sqrt((points[i][0]**2)+(points[i][1]**2))
            # print(distance)
            distances.append(distance)

        # now we sort distances
        sorted_distances = sorted(range(len(distances)), key=lambda k: distances[k])

        for i in range(K):
            ans.append(points[sorted_distances[i]])

        return ans


def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

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
            points = stringToInt2dArray(line)
            line = next(lines)
            K = stringToInt(line)

            ret = Solution().kClosest(points, K)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
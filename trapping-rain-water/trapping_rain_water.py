import json

class Solution_Slow(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_wall_height = 0
        total_water_trapped = 0
        for i in range(len(height)):
            # print("height of column " + str(i) + " = " + str(height[i]))
            if height[i] > left_wall_height:
                # current height is bigger than left wall, so no water can be trapped here
                left_wall_height = height[i]
                continue
            elif height[i] == left_wall_height:
                # same height to the left wall, so no water can be trapped here
                continue
            elif i == len(height)-1:
                # we are at the right corner, so no water can be trapped here
                continue
            else:
                # left wall is higher, so we can potentially trap water here
                right_wall_height = max(height[i+1:len(height)+1])
                # print("left_wall_height: " + str(left_wall_height))
                # print("right_wall_height: " + str(right_wall_height))
                if min(right_wall_height,left_wall_height) > height[i]:
                    water_trapped = min(right_wall_height,left_wall_height) - height[i]
                    # print("water trapped here: " + str(water_trapped))
                    total_water_trapped += water_trapped

        return total_water_trapped


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1
        total_water_trapped = 0

        while left < right:
            # print("left: " + str(left) + ", right: " + str(right))
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total_water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    total_water_trapped += right_max - height[right]
                right -= 1

        return total_water_trapped


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
            height = stringToIntegerList(line)
            print("height: " + str(height))

            ret = Solution().trap(height)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
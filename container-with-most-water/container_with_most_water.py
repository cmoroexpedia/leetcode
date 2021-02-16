import json

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        iterations = 0
        i = 0
        j = len(height)-1

        while i != j:
            iterations +=1
            print "---"
            print "i:" + str(i) + ", j:" + str(j)
            print "values: " + str(height[i]) + "," + str(height[j])
            min_height = min(height[i],height[j])
            print "min height: " + str(min_height)
            print "area = " + str(j-i) + " * " + str(min_height)
            area = (j-i)*min_height
            print "area = " + str(area)
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        print "iterations: " + str(iterations)
        return max_area


class Solution_Slow(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        iterations = 0

        for i in range(0,len(height)):
            print "------------"
            if (len(height) - i) * height[i] <= max_area:
                continue
            for j in reversed(range(i+1,len(height))):
                iterations +=1
                print "---"
                print "i:" + str(i) + ", j:" + str(j)
                print "values: " + str(height[i]) + "," + str(height[j])
                min_height = min(height[i],height[j])
                print "min height: " + str(min_height)
                print "area = " + str(j-i) + " * " + str(min_height)
                area = (j-i)*min_height
                print "area = " + str(area)
                if area > max_area:
                    max_area = area
        print "iterations: " + str(iterations)
        return max_area

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
            print "**************************** start *******************************"
            line = lines.next()
            height = stringToIntegerList(line)
            print "height: " + str(height)
            ret = Solution().maxArea(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
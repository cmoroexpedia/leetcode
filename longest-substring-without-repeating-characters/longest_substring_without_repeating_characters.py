import heapq


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # this will keep the longest substring found
        longestSubstring = 0

        # this will keep a list of existing seen chars
        seen = {}

        # this will keep the length of current substring
        substringSize = 0

        # this will keep the index of last duplicate char seen
        lastDupSeen = 0

        for index,char in enumerate(s):

            if char in seen:
                lastDupSeen = max(seen[char],lastDupSeen)
                substringStart = lastDupSeen + 1
                # if char has been seen before, reset string size to size of substring from the last time the char was seen
                substringSize = index - substringStart + 1
            else:
                substringSize += 1

            if substringSize>longestSubstring:
                longestSubstring = substringSize

            # adding char to dict of seen chars
            seen[char] = index

            # print("s[{}]={}".format(index,char))
            # print("last duplicate seen: " + str(lastDupSeen))
            # print("current substring start: " + str(substringStart))
            # print("current substring size: " + str(substringSize))
            # print("current longest substring: " + str(longestSubstring))

        return max(longestSubstring, substringSize)


class Solution_Optimal(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = -1
        recent = -1
        max_len = 0
        pos = {}

        for sub in s:
            index += 1
            if sub in pos:
                if (index - 1 - recent > max_len):
                    max_len = index - 1 - recent
                if (pos[sub] > recent):
                    recent = pos[sub]
            pos[sub] = index

        if (index - recent > max_len):
            max_len = index - recent

        return max_len

        print("start")
        print(sub)
        print(index)
        print(recent)
        print(max_len)


class SolutionMaxHeap(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # this will keep a max heap of longest substring found
        longestSubstring = []

        # this will keep a list of existing seen chars
        seen = []

        # this will keep the length of current substring
        substringSize = 0

        for char in s:
            # print("current char: " + char)

            if char not in seen:
                substringSize += 1
            else:
                # add to longest substring max heap the current size and reset to zero
                heapq.heappush(longestSubstring, self.toggleSign(substringSize))
                substringSize = 1
                seen = []
            # print("current substring size: " + str(substringSize))

            # adding char to list
            seen.append(char)

        # avoid IndexError when max heap is null
        try:
            longest = self.toggleSign(heapq.heappop(longestSubstring))
        except IndexError:
            longest = 0

        return max(longest, substringSize)

    def toggleSign(self,num):
        return num * -1




def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            line = next(lines)
            s = stringToString(line)
            print("***************************************** start ***********************************************")
            print("string: " + s)

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
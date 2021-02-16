import json


class Solution_Optimal(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if strs == [] or len(strs) == 0:
            return res
        strs.sort()
        first = list(strs[0])
        last = list(strs[-1])
        for i in range(len(first)):
            if len(last) > i and first[i] == last[i]:
                res += first[i]
            else:
                return res
        return res


# Definition for a dictionary tree.
class DictionaryNode(object):
    def __init__(self):
        self.isWord = False
        self.occurrences = 0
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None
        self.h = None
        self.i = None
        self.j = None
        self.k = None
        self.l = None
        self.m = None
        self.n = None
        self.o = None
        self.p = None
        self.q = None
        self.r = None
        self.s = None
        self.t = None
        self.u = None
        self.v = None
        self.w = None
        self.x = None
        self.y = None
        self.z = None

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        global longest_size
        global longest_string
        longest_string = ""
        longest_size = 0

        def traverseTree (current_string, node):
            print "current string: " + current_string + " (" + str(node.occurrences) + ")"
            global longest_size
            global longest_string

            if node.occurrences == len(strs):
                size = len(current_string)
                print "found common prefix '" + current_string + "' of size " + str(size)
                if size > longest_size:
                    longest_size = size
                    longest_string = current_string

            if node.isWord:
                print "^^^ is a word"

            for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                if getattr(node,char):
                    traverseTree(current_string+char,getattr(node,char))


        # create root node
        root = DictionaryNode()

        # load strings in tree
        for string in strs:
            print "adding string '" + string + "' to tree"
            # pointer to traverse tree
            ptr = root
            for i, char in enumerate(string):
                # print "adding char '" + char + "' to tree"
                if getattr(ptr,char):
                    pass
                    # print "found char '" + char
                else:
                    setattr(ptr,char,DictionaryNode())
                ptr = getattr(ptr, char)
                ptr.occurrences += 1
                if i == len(string)-1:
                    ptr.isWord = True


        # traversing tree (just or fun)
        print "traversing tree"
        traverseTree("",root)

        return longest_string





def stringToStringArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print "******************************************************************************"
            line = lines.next()
            strs = stringToStringArray(line)
            print "strings: " + str(strs)

            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()

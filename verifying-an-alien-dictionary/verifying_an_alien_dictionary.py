import json

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        orderDict = {}
        # create hashmap with order of alien dictionary
        for i in range(len(order)):
            orderDict[order[i]] = i
        # print orderDict

        if len(words) == 1:
            return True

        # starting from second word, always comparing to the previous one
        i = 1
        while i < len(words):
            currentWord = words[i]
            previousWord = words[i-1]
            # print "current word: {}".format(currentWord)
            # print "previous word: {}".format(previousWord)

            j = 0
            while j < min(len(previousWord),len(currentWord)):
                currentChar = currentWord[j]
                previousChar = previousWord[j]
                j += 1
                # print "current char: {}".format(currentChar)
                # print "previous char: {}".format(previousChar)
                if orderDict[currentChar] < orderDict[previousChar]:
                    print "returning false"
                    return False
                elif orderDict[currentChar] == orderDict[previousChar]:
                    continue
                else:
                    break

            # reached end of comparison. Need to compare if second word is larger and return false (e.g ["apple","app"])
            if currentChar == previousChar:
                if len(currentWord) < len(previousWord):
                    return False

            i += 1

        # if I made until here it's because all words are equal
        return True

def stringToStringArray(input):
    return json.loads(input)

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        print "**************************** start *******************************"
        try:
            line = lines.next()
            words = stringToStringArray(line)
            print "words: {}".format(words)
            line = lines.next()
            order = stringToString(line)
            print "order: {}".format(order)

            ret = Solution().isAlienSorted(words, order)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
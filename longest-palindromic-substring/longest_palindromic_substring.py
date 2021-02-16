class Solution_Optimal(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            palindrome = self.palinDrome(s,i,i)
            if len(palindrome)>len(ans):
                ans = palindrome

            palindrome = self.palinDrome(s,i,i+1)
            if len(palindrome)>len(ans):
                ans = palindrome

        return ans

    def palinDrome(self,s,start,end):
        while(start>=0 and end<len(s)) and s[start]==s[end]:
            start = start-1
            end = end+1

        return s[start+1:end]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""
        longest_size = 0

        if len(s) > 0:
            longest = s[0]
            longest_size = 1

        for index, char in enumerate(s):
            # print("---------")
            # print("current char (s[{}]): ".format(index) + char)
            max_possible = min(index,len(s)-index-1)
            # print("maximum palindrome size: " + str(max_possible))
            for i in range(1,max_possible+1):
                current_prefix = s[index-i]
                # print("current prefix: " + str(current_prefix))
                current_sufix = s[index+i]
                # print("current sufix: " + str(current_sufix))
                if current_prefix == current_sufix:
                    palindrome_size = i*2+1
                    # print("WE HAVE A MATCH OF SIZE: " + str(palindrome_size))
                    palindrome_str = s[index-i:index] + char + s[index+1:index+i+1]
                    # print("palindrome: " + palindrome_str)
                    if palindrome_size > longest_size:
                        longest_size = palindrome_size
                        longest = palindrome_str
                else:
                    # print("break")
                    break
            # print("now including the current char...")
            max_possible = min(index+1,len(s)-index-1)
            # print("maximum palindrome size: " + str(max_possible))
            for i in range(1,max_possible+1):
                current_prefix = s[index-i+1]
                # print("current prefix: " + str(current_prefix))
                current_sufix = s[index+i]
                # print("current sufix: " + str(current_sufix))
                if current_prefix == current_sufix:
                    palindrome_size = i*2
                    # print("WE HAVE A MATCH OF SIZE: " + str(palindrome_size))
                    palindrome_str = s[index-i+1:index+1] + s[index+1:index+i+1]
                    # print("palindrome: " + palindrome_str)
                    if palindrome_size > longest_size:
                        longest_size = palindrome_size
                        longest = palindrome_str
                else:
                    # print("break")
                    break

        return longest


class Solution_Slow(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""
        longest_size = 0

        if len(s) > 0:
            longest = s[0]
            longest_size = 1

        for index, char in enumerate(s):
            # print("---------")
            # print("current char (s[{}]): ".format(index) + char)
            max_possible = min(index,len(s)-index-1)
            # print("maximum palindrome size: " + str(max_possible))
            for i in range(1,max_possible+1):
                current_prefix = s[index-i:index]
                # print("current prefix: " + str(current_prefix))
                current_sufix = s[index+1:index+i+1]
                # print("current sufix: " + str(current_sufix))
                inverted_sufix = current_sufix[::-1]
                # print("current inverted sufix: " + str(inverted_sufix))
                if current_prefix == inverted_sufix:
                    palindrome_size = i*2+1
                    # print("WE HAVE A MATCH OF SIZE: " + str(palindrome_size))
                    palindrome_str = current_prefix + char + current_sufix
                    # print("palindrome: " + palindrome_str)
                    if palindrome_size > longest_size:
                        longest_size = palindrome_size
                        longest = palindrome_str
            # print("now including the current char...")
            max_possible = min(index+1,len(s)-index-1)
            # print("maximum palindrome size: " + str(max_possible))
            for i in range(1,max_possible+1):
                current_prefix = s[index-i+1:index+1]
                # print("current prefix: " + str(current_prefix))
                current_sufix = s[index+1:index+i+1]
                # print("current sufix: " + str(current_sufix))
                inverted_sufix = current_sufix[::-1]
                # print("current inverted sufix: " + str(inverted_sufix))
                if current_prefix == inverted_sufix:
                    palindrome_size = i*2
                    # print("WE HAVE A MATCH OF SIZE: " + str(palindrome_size))
                    palindrome_str = current_prefix + current_sufix
                    # print("palindrome: " + palindrome_str)
                    if palindrome_size > longest_size:
                        longest_size = palindrome_size
                        longest = palindrome_str

        return longest

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print("**************************** start *******************************")
            line = next(lines)
            s = stringToString(line)
            print("string to be processed: " + s)

            ret = Solution().longestPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

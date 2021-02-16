class Solution_Optimal(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # sample code
        # two_dimension_array = [['p','a','h','n'],
        #                        ['a','p','l','s','i','g'],
        #                        ['y','i','r']
        #                        ]
        #
        # for row in range(len(two_dimension_array)):
        #     for col in range(len(two_dimension_array[row])):
        #         print("two_dimension_array[{}][{}] = ".format(row,col) + two_dimension_array[row][col])

        result = ""
        result_array = [[]*numRows for x in range(numRows)]
        zig_zag_size = self.get_zig_zag_size(numRows)
        # print("zig zag size: " + str(zig_zag_size))

        for index, char in enumerate(s):
            # print("current: s[{}]={}".format(index,char))
            zig_zag_row = self.get_row_to_append(index, numRows, zig_zag_size)
            # print("zig zag row: " + str(zig_zag_row))
            result_array[zig_zag_row].append(char)

        # fetch results
        for row in range(len(result_array)):
            for col in range(len(result_array[row])):
                # print("two_dimension_array[{}][{}] = ".format(row,col) + result_array[row][col])
                result += result_array[row][col]

        return result

    def get_row_to_append(self, index, num_rows, zig_zag_size):
        zig_zag_pos = index % zig_zag_size
        if zig_zag_pos < num_rows:
            return zig_zag_pos
        else:
            return num_rows-(zig_zag_pos+1-num_rows)-1


    def get_zig_zag_size(selfs, numRows):
        if numRows>1:
            return (numRows) + (numRows-2)
        else:
            return numRows


def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToInt(input):
    return int(input)

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
            line = next(lines)
            numRows = stringToInt(line)
            print("number of rows: " + str(numRows))

            ret = Solution().convert(s, numRows)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
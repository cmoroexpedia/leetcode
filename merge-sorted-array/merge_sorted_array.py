import json

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # make a copy of nums1
        nums1_copy = nums1[:m]
        # print("nums1_copy: " + str(nums1_copy))

        # create pointers to track position for nums1, nums2 and results
        nums1_pointer = 0
        nums2_pointer = 0
        res_pointer = 0

        while res_pointer < n+m:
            # print("nums1_pointer: " + str(nums1_pointer))
            # print("nums2_pointer: " + str(nums2_pointer))
            # print("res_pointer: " + str(res_pointer))


            if nums1_pointer == m:
            # reached the end of nums1; just use nums2 for the remaining iterations
                nums1[res_pointer] = nums2[nums2_pointer]
                nums2_pointer += 1
                res_pointer +=1
                continue
            if nums2_pointer == n:
                # reached the end of nums2; just use nums1 for the remaining iterations
                nums1[res_pointer] = nums1_copy[nums1_pointer]
                nums1_pointer += 1
                res_pointer +=1
                continue

            if nums1_copy[nums1_pointer] <= nums2[nums2_pointer]:
                nums1[res_pointer] = nums1_copy[nums1_pointer]
                nums1_pointer += 1
            else:
                nums1[res_pointer] = nums2[nums2_pointer]
                nums2_pointer += 1
            res_pointer +=1






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
            print("********************** start ************************")
            line = next(lines)
            nums1 = stringToIntegerList(line)
            print("nums1: " + str(nums1))
            line = next(lines)
            m = stringToInt(line)
            print("m: " + str(m))
            line = next(lines)
            nums2 = stringToIntegerList(line)
            print("nums2: " + str(nums2))
            line = next(lines)
            n = stringToInt(line)
            print("n: " + str(n))

            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print("Do not return anything, modify nums1 in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
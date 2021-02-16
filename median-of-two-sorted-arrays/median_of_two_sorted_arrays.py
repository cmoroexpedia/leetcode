import json

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        combined_array = sorted(nums1 + nums2)
        # print "combined array: " + str(combined_array)

        # now I need to find the median
        if len(combined_array) % 2 == 0:
            # print "array size (" + str(len(combined_array)) + ") is even number"
            median_index1 = len(combined_array)/2 - 1
            median_index2 = median_index1 + 1
            # print "median index 1: " + str(median_index1)
            # print "median index 2: " + str(median_index2)
            # print "median: " + str(combined_array[median_index1]) + " + " + str(combined_array[median_index2]) + " / 2"
            median = (combined_array[median_index1] + combined_array[median_index2]) / 2.0
        else:
            # print "array size (" + str(len(combined_array)) + ") is odd number"
            median_index = abs(len(combined_array)/2)
            median = combined_array[median_index]

        return median


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


class Solution_Optimal(object):

    def findMedianSortedArrays(self, nums1, nums2):
        (bigger, smaller, m, n) = (nums1, nums2, len(nums1), len(nums2)) if len(nums1) > len(nums2) else (nums2, nums1, len(nums2), len(nums1))
        min_index, max_index = 0, len(smaller)
        median = None

        while min_index <= max_index:
            i = (min_index+max_index)/2
            j = ((n+m+1)/2)-i
            if j < m and i > 0 and smaller[i-1] > bigger[j]:
                max_index = i-1
            elif i < n and j > 0 and bigger[j-1] > smaller[i]:
                min_index = i+1
            else:
                if i == 0:
                    median = bigger[j-1]
                elif j == 0:
                    median = smaller[i-1]
                else:
                    median = max(smaller[i-1], bigger[j-1])

                break
        if (n+m) % 2 == 1:
            return median
        if i == n:
            return (median + bigger[j])/2.0
        if j == m:
            return (median + smaller[i])/2.0
        return (median + min(smaller[i], bigger[j]))/2.0


class Solution_Optimal2(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)


def stringToIntegerList(input):
    return json.loads(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print "******************************** start ***************************************"
            line = lines.next()
            nums1 = stringToIntegerList(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
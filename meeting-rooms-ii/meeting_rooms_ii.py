import json

class Solution_Bruteforce(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        # DOES NOT WORK!
        # NEED TO CHECK IF OTHER CONFLICTING ROOMS ARE AVAILAVLE TOO!

        if intervals is None or len(intervals) == 0:
            return 0

        ans = 0

        i = 0
        while i < len(intervals):
            conflicts = 0
            j = 0
            while j < len(intervals):
                # print("Checking intervals: {} and {}".format(intervals[i],intervals[j]))
                # check if intervals conflict
                if intervals[i][0] <= intervals[j][0]:
                    # meeting i starts before or at the same time as meeting j
                    if intervals[j][0] < intervals[i][1]:
                        conflicts += 1
                        # print("conflict! number of conflicts is now {}".format(conflicts))
                else:
                    # meeting j starts before meeting j
                    if intervals[i][0] < intervals[j][1]:
                        conflicts += 1
                        # print("conflict! number of conflicts is now {}".format(conflicts))

                if conflicts > ans:
                    ans = conflicts
                j += 1
            i += 1

        return ans


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if intervals is None or len(intervals) == 0:
            return 0

        # sorting intervals so we can loop through them in one pass
        intervals.sort()
        print("Sorted intervals: " + str(intervals))

        # initializing conf_rooms with end time of first meeting of the day
        conf_rooms = [intervals[0][1]]

        i = 1
        while i < len(intervals):
            # print(intervals[i])
            # check if starting time of current meeting is less than
            # minimum end time of all conf_rooms
            if intervals[i][0] < min(conf_rooms):
                # we need another conf room
                # print("we need a new conf room")
                conf_rooms.append(intervals[i][1])
            else:
                # we don't need a new conf room
                # print("we don't need a new conf room")
                # update conf_rooms with new end time
                conf_rooms[conf_rooms.index(min(conf_rooms))] = intervals[i][1]
            i += 1

        return len(conf_rooms)

def stringToInt2dArray(input):
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
            intervals = stringToInt2dArray(line)
            print(intervals)

            ret = Solution().minMeetingRooms(intervals)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
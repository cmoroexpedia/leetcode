import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummyRoot = ListNode(0)
        ptr = dummyRoot

        if not l1 or not l2: return l1 or l2

        while l1 or l2:
            # print "*************************"
            if not l1:
                ptr.next = ListNode(l2.val)
                ptr = ptr.next
                l2 = l2.next
                continue
            if not l2:
                ptr.next = ListNode(l1.val)
                ptr = ptr.next
                l1 = l1.next
                continue

            # print("l1.val: " + str(l1.val))
            # print("l2.val: " + str(l2.val))

            if (l1.val <= l2.val):
                ptr.next = ListNode(l1.val)
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                ptr = ptr.next
                l2 = l2.next

        ptr = dummyRoot.next
        return ptr


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            print "======================================="
            line = lines.next()
            l1 = stringToListNode(line)
            print listNodeToString(l1)
            line = lines.next()
            l2 = stringToListNode(line)
            print listNodeToString(l2)

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
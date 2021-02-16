import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_Optimal(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2: return l1 or l2
        carry, ans = 0, l1

        while l1 or l2:
            total = l1.val + carry + (0 if not l2 else l2.val)
            l1.val, carry = total % 10, total // 10
            previous = l1
            if not l1.next:
                if l2 and l2.next: l1.next = l2.next
            l1 = l1.next
            l2 = l2.next if (l2 and l1 != l2.next) else None
        if carry:
            previous.next = ListNode(carry)
        return ans


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum = l1.val + l2.val
        # print("sum: " + str(sum))
        if sum>=10:
            sum = sum - 10
            carryover = 1
        else:
            carryover = 0
        result = ListNode(sum)
        ptr = result
        # print("current result: " + listNodeToString(result))

        while l1.next or l2.next or carryover==1:
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0

            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0

            sum = l1.val + l2.val + carryover
            # print("sum: " + str(sum))
            if sum>=10:
                sum = sum - 10
                carryover = 1
            else:
                carryover = 0

            ptr.next = ListNode(sum)
            ptr = ptr.next

        return result



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
            print("********************** start ************************")
            line = next(lines)
            l1 = stringToListNode(line)
            print(listNodeToString(l1))
            line = next(lines)
            l2 = stringToListNode(line)
            print(listNodeToString(l2))

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
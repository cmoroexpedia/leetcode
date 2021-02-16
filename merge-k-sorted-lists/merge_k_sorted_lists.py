import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None





class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummyRoot = ListNode(0)
        ptr = dummyRoot

        # for list in lists:
        #     print("traversing list")
        #     travereLinkedList(list)


        # fetching first element of each list
        head = []
        for list in lists:
            if list is not None:
                head.append(list.val)
            else:
                head.append(None)

        # pointers to current node
        currNode = []
        for list in lists:
            currNode.append(list)

        # getting min val from head
        try:
            minVal = min(i for i in head if i is not None)
        except ValueError:
            # all values are None
            minVal = None

        while minVal is not None:
            # print("head: {}".format(head))
            # print("minVal: {}".format(minVal))
            # print("minValIndex: {}".format(head.index(minVal)))
            headIndex = head.index(minVal)
            minNode = ListNode(minVal)
            ptr.next = minNode
            ptr = minNode
            currNode[headIndex] = currNode[headIndex].next
            if currNode[headIndex] is not None:
                head[headIndex] = currNode[headIndex].val
            else:
                head[headIndex] = None
            try:
                minVal = min(i for i in head if i is not None)
            except ValueError:
                "all none"
                minVal = None


        return dummyRoot.next



def travereLinkedList(list):

    ptr = list
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next



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

def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes

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
            print("**************************** start *******************************")
            line = next(lines)
            lists = stringToListNodeArray(line)

            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
import json


class Solution:
    def solve(self, prices: list[int]) -> int:
        # default to zero profit
        solution = 0

        # solve in one pass
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > solution:
                solution = prices[i] - min_price
        return solution


class SolutionEvenWorse:
    def solve(self, prices: list[int]) -> int:
        # default to zero profit
        solution = 0

        # make a copy of prices and sort it retaining original index
        sorted_prices = []
        for i in range(len(prices)):
            sorted_prices.append([prices[i],i])
        sorted_prices.sort()
        #print('sorted prices with original indexes: {}'.format(sorted_prices))

        # start comparing leftmost with rightmost element moving inward
        left = 0
        right = len(sorted_prices) - 1

        while right > left:
            maximum_profit = sorted_prices[right][0]-sorted_prices[left][0]
            if maximum_profit < solution:
                break
            #print('maximum profit on this iteration: {}'.format(maximum_profit))

            # start comparing left with right elements in right to left order
            for i in range(right, left, -1):
                possible_profit = sorted_prices[i][0]-sorted_prices[left][0]
                if possible_profit < solution:
                    break
                #print('LEFT: comparing {} with {}'.format(sorted_prices[left],sorted_prices[i]))
                # check if buy date is before sell date and save profit
                if sorted_prices[left][1] < sorted_prices[i][1]:
                    #print('found possible profit of: {}'.format(possible_profit))
                    if possible_profit > solution:
                        solution = possible_profit
            # now compare right with left elements in left to right order
            for i in range(left+1, right):
                possible_profit = sorted_prices[right][0]-sorted_prices[i][0]
                if possible_profit < solution:
                    break
                #print('RIGHT: comparing {} with {}'.format(sorted_prices[i],sorted_prices[right]))
                # check if buy date is before sell date and save profit
                if sorted_prices[i][1] < sorted_prices[right][1]:
                    #print('found possible profit of: {}'.format(possible_profit))
                    if possible_profit > solution:
                        solution = possible_profit

            right -= 1
            left +=1

        return solution


class SolutionSlow:
    def solve(self, prices: list[int]) -> int:
        # default to zero profit
        solution = 0

        # brute force solution
        for i in range(len(prices)):
            # check the current price with all future days and save the maximum profit
            for j in range(i+1,len(prices)):
                #print('comparing buy:{} with sel:{}'.format(prices[i],prices[j]))
                profit = prices[j] - prices[i]
                if profit > solution:
                    #print('found better profit at buy:{} and sell:{}'.format(prices[i],prices[j]))
                    solution = profit

        return solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Other code snippets
def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def stringToBool(input):
    return json.dumps(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def stringToString(input):
    return json.loads(input)


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


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
            line = next(lines)
            print("********************** start ************************")
            input = stringToIntegerList(line)
            print("input: " + str(input))

            ret = Solution().solve(input)

            out = intToString(ret)
            print("output: " + out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

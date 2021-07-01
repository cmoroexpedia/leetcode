import json


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        solution = None

        # initializing initial position and distance to base
        position = [0,0]
        distance = 0

        # initializing direction
        direction = "north"

        # maximum number of iterations
        max_iterations = 4

        for i in range(max_iterations):
            # iterate over instructions and execute them one by one
            print('****** iteration: {} ******'.format(i+1))
            for instruction in instructions:
                print('-->Instruction: {}'.format(instruction))
                position, direction = self.options[instruction](self, position, direction)
                print('New position: {}'.format(position))
                print('New direction: {}'.format(direction))

            if position == [0,0]:
                # returned to base so this is definitely a circular instruction
                return True

            #distance = self.distance_to_base(position)
            #print('distance to base after iteration: {}'.format(distance))


        return solution

    def distance_to_base(self, position):
        import numpy as np

        # intializing points in numpy arrays
        point1 = np.array((0, 0))
        point2 = np.array((position[0], position[1]))

        # finding sum of squares
        sum_sq = np.sum(np.square(point2 - point1))

        # Doing squareroot and printing Euclidean distance
        distance = np.sqrt(sum_sq)
        print('Distance to base: {}'.format(distance))
        return distance


    def G(self, position, direction):
        # implement instruction G
        print('instruction G was executed')
        if direction == "north":
            return [position[0],position[1]+1], direction
        elif direction == "south":
            return [position[0],position[1]-1], direction
        elif direction == "west":
            return [position[0]-1,position[1]], direction
        elif direction == "east":
            return [position[0]+1,position[1]], direction


    def L(self, position, direction):
        # implement instruction L
        print('instruction L was executed')
        if direction == "north":
            return [position[0],position[1]], "west"
        elif direction == "south":
            return [position[0],position[1]], "east"
        elif direction == "west":
            return [position[0],position[1]], "south"
        elif direction == "east":
            return [position[0],position[1]], "north"


    def R(self, position, direction):
        # implement instruction R
        print('instruction R was executed')
        if direction == "north":
            return [position[0],position[1]], "east"
        elif direction == "south":
            return [position[0],position[1]], "west"
        elif direction == "west":
            return [position[0],position[1]], "north"
        elif direction == "east":
            return [position[0],position[1]], "south"

    options = {
        "G" : G,
        "L" : L,
        "R" : R
    }

########################################### END OF SOLUTION CODE #######################################################


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


def boolToString(input):
    if input is None:
        input = False
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
            input = stringToString(line)
            print("input: " + str(input))
            ret = Solution().isRobotBounded(input)

            out = boolToString(ret)
            print("output: " + out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

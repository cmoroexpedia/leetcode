
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # print("Traverse Recursive:")
        # traverseTreeRecursive(root)
        # print("Traverse InOrder:")
        # traverseInOrder(root)
        # print("Traverse PreOrder:")
        # traversePreOrder(root)

        self.ans = 1
        def treeDepth(root):

            if root == None:
                # if reached a null node, return depth of zero
                return 0

            if root.left == None and root.right == None:
                # reached a leaf, return depth of one
                return 1

            L = treeDepth(root.left)
            R = treeDepth(root.right)

            currentDepth = L + R + 1
            if currentDepth > self.ans:
                self.ans = currentDepth

            return max(L,R) + 1

        treeDepth(root)
        return self.ans - 1


def traverseTreeRecursive(root):

    # Preorder
    print("val: " + str(root.val))

    if root.left == None and root.right == None:
        # reached a leaf
        # print("Found a leaf! (val: " + str(root.val) + ")")
        return

    traverseTreeRecursive(root.left)
    traverseTreeRecursive(root.right)

def traverseInOrder(root):

    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.val)

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break


def traversePreOrder(root):

    # Set current to root of binary tree
    stack = [root] # initialize stack
    current = None

    while (len(stack) > 0):

        current = stack.pop()
        print(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


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
            root = stringToTreeNode(line)

            ret = Solution().diameterOfBinaryTree(root)

            out = intToString(ret)
            print("out: " + str(out))
        except StopIteration:
            break

if __name__ == '__main__':
    main()
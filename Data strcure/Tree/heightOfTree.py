from sys import stdin, stdout

class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None
        self.level = None

class BST:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left is None:
                        current.left = Node(val)
                    else:
                        current = current.left
                elif val > current.info:
                    if current.right is None:
                        current.right = Node(val)
                    else:
                        current = current.right
                else:
                    break


def heightOfTree(root):
    if root:
        if root.left or root.right:
            return (max(heightOfTree(root.left), heightOfTree(root.right)) + 1)
        else:
            return max(heightOfTree(root.left), heightOfTree(root.right))
    else:
        return 0

t = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

tree = BST()

for i in range(t):
    tree.create(arr[i])

print(heightOfTree(tree.root))





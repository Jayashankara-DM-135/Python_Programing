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


def preOrderTraversal(root):
    if root:
        print(root.info, end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.info, end=" ")
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.info, end=" ")


t = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

tree = BST()

for i in range(t):
    tree.create(arr[i])
stdout.write("Pre order traversal\n")
preOrderTraversal(tree.root)
stdout.write("\n In order traversal\n")
inOrderTraversal(tree.root)
stdout.write("\n Post order traversal\n")
postOrderTraversal(tree.root)




from sys import stdin, stdout
from collections import deque

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


def levelOrderTraversal(root):
    d = deque()
    d.append(root)

    while d:
        temp = d.popleft()
        print(temp.info, end=" ")
        if temp.left:
            d.append(temp.left)
        if temp.right:
            d.append(temp.right)

t = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

tree = BST()

for i in range(t):
    tree.create(arr[i])

levelOrderTraversal(tree.root)





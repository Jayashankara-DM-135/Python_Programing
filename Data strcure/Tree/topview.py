from sys import stdin, stdout
from collections import deque
from collections import defaultdict

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

def topview(root):
    if root is None:
        return

    d = deque()
    hd = 0
    root.hd = hd
    d.append(root)
    m = defaultdict(int)

    while d:
        temp = d.popleft()
        hd = temp.hd
        if hd not in m:
            m[hd] = temp.info
        if temp.left:
            temp.left.hd = hd - 1
            d.append(temp.left)
        if temp.right:
            temp.right.hd = hd+1
            d.append(temp.right)

    print(m)
    for x in sorted(m):
        print(m[x], end=" ")



t = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

tree = BST()

for i in range(t):
    tree.create(arr[i])

topview(tree.root)





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

def printVerticalOrdering(root, hd, m):
    if root:
        m[hd].append(root.info)
        printVerticalOrdering(root.left, hd-1, m)
        printVerticalOrdering(root.right, hd + 1, m)

# No need to be BST, It can be normal tree as well.
def verticalOrderTraversal(root):
    hd = 0
    mydict = defaultdict(list)
    mydict[hd].append(root.info)
    printVerticalOrdering(root.left, hd -1 , mydict)
    printVerticalOrdering(root.right, hd + 1 , mydict)
    print(mydict)

    for i in sorted(mydict):
        for x in mydict[i]:
            print(x, end=" ")
        print("")
        #print(x for x in mydict[i] , end=" ")




t = int(stdin.readline())
arr = list(map(int, stdin.readline().strip().split()))

tree = BST()

for i in range(t):
    tree.create(arr[i])

verticalOrderTraversal(tree.root)





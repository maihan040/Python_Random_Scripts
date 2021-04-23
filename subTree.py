#!/usr/bin/python3

#define the node class
class Node: 
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


def inOrder(root): 
    if root == None: 
        return ''

    #local variables
    s = []
    treeString = ''
    current = root

    while True: 
        if current: 
            s.append(current)
            current = current.left
        elif(s):
            current = s.pop()
            treeString += str(current.val)
            current = current.right
        else: 
            break
    return treeString

def find_substring(s, t): 
    if s == None and t != None: 
        return True
    if s != None and t == None: 
        return False

    subTree = inOrder(s)
    tree = inOrder(t)
    idx = tree.find(subTree)

    if idx >= 0: 
        return True
    else: 
        return False

#main 
left = Node(4, Node(3), Node(2))
right = Node(5, Node(4), Node(-1))
t = Node(1, left, right)
s = Node(1, Node(4), Node(5))

subTree = inOrder(s)
tree = inOrder(t)

print("Tree is : " + tree)
print("Subtree is : " + subTree)


result = find_substring(s, t)
if result:
    print("Subtree found")
else: 
    print("Subtree not found")

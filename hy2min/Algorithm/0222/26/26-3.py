class Node:
    def __init__(self,x):
        self.x = x
        self.next = None

a = Node(3)
b = Node(5)
c = Node(4)

a.next = b
c.next = c

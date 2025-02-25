class Node:
    def __init__(self,age):
        self.age = age
        self.next1 = None
        self.next2 = None

simson = Node(20)
woman1 = Node(29)
woman2 = Node(30)

man1 = Node(25)
man2 = Node(40)
man3 = Node(38)

simson.next1 = woman1
simson.next2 = woman2
woman1.next1 = man1
woman1.next2 = man2
woman2.next1 = woman1
woman2.next2 = man3
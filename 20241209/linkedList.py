class Node : 
    def __init__(self,val,next=None):
        self.val = val,
        self.next = next

Head = Node(1)
middleNode = Node(2)
lastNode = Node(3)

Head.next = middleNode
middleNode.next = lastNode


class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


head = Node(10)

a = Node(11)
head.next = a

b = Node(12)
a.next = b

def travel(head,targetVal):

    temp = head

    while temp:
        if targetVal == temp.value:
            return True
        
        temp = temp.next
        
    return False

# print(travel(head,11))


def insert(head,val,position):
    temp = head
    p = 1

    while temp:
        if p == position:
            prevPoint = temp.next
            newPoint = Node(val,prevPoint)
            temp.next = newPoint
            return "New Node added!"
        p+=1
        temp = temp.next

    return "Position not found!"

print(insert(head,10,12))

print(head.next.next)
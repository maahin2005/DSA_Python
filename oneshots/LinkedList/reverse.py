class SinglyNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


head = SinglyNode(1)
a = SinglyNode(2)
b = SinglyNode(3)


head.next = a
a.next = b

def travel(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.value))
        curr = curr.next
    return " -> ".join(ele)

# print(travel(head))

def reverse(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
newHead = reverse(head)

# print("newHead: ",newHead.value)
print("Travel: ",travel(newHead))
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


Head = Node(1)

A = Node(2)

B = Node(2)

C = Node(1)

Head.next = A
A.next = B
B.next = C
# 1 -> 2 -> 2 -> 1



def lenLL(head):
    count = 0
    curr = head

    while curr:
        curr = curr.next
        count += 1
    
    return count

def midLL(length):
    return length // 2
    
length = lenLL(Head)
mid = midLL(length)
print(length, mid)

def isPalindrome(head):
    pass
### Leetcode problem - Reverse the Singly Linked List

=> How to reverse the Singly Linked List:

Inout: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

head = 1
i want my head should be -> 5

prev = None
curr => will point curr position (where I am) = head

next_node = curr.next
curr.next = prev
prev = curr
curr = next_node

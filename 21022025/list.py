# LIST

my_list = [1,2,3]
print("my_list: ", my_list)


# Append any value at the end of the list
my_list.append(4)
print("After appending value in my_list: ", my_list)

# Extending List
my_list.extend([5,6])
print("After extend: my_list: ", my_list)

# Pop from the List
# if there is no any index passed to the pop function so it will remove item from the end 
# otherwise will remove passed index
my_list.pop()
print("After POP-witout passing index: my_list: ", my_list)
my_list.pop(3)
print("After POP-with passing index: my_list: ", my_list)

# Insert into list
index = 3
value = 4
my_list.insert(index,value)
print("After insert: my_list: ", my_list)

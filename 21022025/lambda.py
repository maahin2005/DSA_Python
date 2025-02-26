add = lambda x,y: x + y
result = add(1,2)
print(result)

sub = lambda x,y:x-y
result = sub(4,2)
print(result)

numbers = [1,2,3,4,5]
result = list(map(lambda x: x**2, numbers))
print(result)


numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

from functools import reduce
numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)  # 10
print("sum_all: " , sum_all)

numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers) 
print("sorted_numbers: " , sorted_numbers)

words = ["a", "abc", "de"]
sorted_words = sorted(words, key=lambda x:len(x))
print("sorted_words: " , sorted_words)

def custom_sort(x):
    return x % 3

numbers = [1, 2, 3, 4, 5, 6]
sorted_numbers = sorted(numbers, key=custom_sort)  
print("custom sorted: sorted_numbers: " , sorted_numbers)

import random

# generate two random lists of numbers
list1 = [random.randint(0, 9999) for _ in range(random.randint(50, 100))]
list2 = [random.randint(0, 9999) for _ in range(random.randint(50, 100))]

# print the two lists
print("List 1:", list1)
print("List 2:", list2)

# create a new list of elements common to both lists
result = [x for x in list1 if x in list2]

# print the resulting list
print("Elements common to both lists:", result)
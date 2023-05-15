"""
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect,
 the two names (list_1 and list_2) identify the same location in the computer memory. 
 Modifying one of them affects the other, and vice versa.

Solution to this is slice ([:])
A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
"""
my_list = [99,44,22,11]
print(my_list[:])
# my_list[start:end]

print(my_list[1:4]) # gets the list from index 1 to index 4-1. It does not include the end index

print(my_list[:3])  # if start value is not provided, it assumes it as 0 so it returns values from 0 to 3

print(my_list[1:])  # if start value is not provided, it assumes it as last index so it returns values from 1 to last

print(my_list[1:-1]) # if negative value is provided it get the value from reverse order

print(my_list[-1:1]) # if a start value is less than the end value, it returns no value


del my_list[1:3]
print(my_list) # deletes the elements from index 1 to index 3-1


del my_list[:] # deletes the contents of the list
del my_list # deletes the whole list, not its contents
print(my_list) # this will give an erro coz there will be no list called my_list
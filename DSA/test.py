import re


my_lst = [x*x for x in range(5)]
print(my_lst)

def f(lst):
    del lst[lst[2]]
    return lst

try:
    print(f(my_lst))
except (ValueError,ZeroDivisionError):
    raise
"""
number of can to paint the wall = (wall height * wall width) / coverage per can
"""


# import math

# def paint_calc(height, width, cover):
#     area = height*width
#     return math.ceil(area/cover)


# print(paint_calc(7,13,5))



"""
Prime number checker
"""

def check_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num} is Prime")
    else:
        print(f'{num} is not a Prime')

check_prime(7)

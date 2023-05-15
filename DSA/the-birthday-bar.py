from operator import indexOf
from tkinter import BitmapImage


def birthday(s, d, m):
    # Write your code here
    
    number_of_ways = 0
    for i in range(len(s)):
        print(f"i: {i}")
        ranged_seq = []
        if len(s)==1:
            print("continue")
        elif i==len(s)-1:
            print("In Break")
            break
        for j in range(i, i+m):
            print(f"j: {j}")
            ranged_seq.append(s[j])
        if ranged_seq is not None:
            print(f"ranged_seq: {ranged_seq}")
            if sum(ranged_seq) == d:
                number_of_ways += 1
    return number_of_ways



seg=[2,2,1,3,2]
date=4
month=2

# seg=[1,2,1,3,2]
# date=3
# month=2

# seg=[1,1,1,1,1,1]
# date=3
# month=2

# seg=[4]
# date=4
# month=1

seg = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
date = 18
month = 7

print(birthday(seg,date,month))
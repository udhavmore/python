"""
11 2 4
4 5 6
10 8 -12
"""

a1 = [11, 2, 4]
a2 = [4, 5, 6]
a3 = [10, 8, -12]

map = [a1, a2, a3]
print(f"{a1}\n{a2}\n{a3}")


def diagonalDifference(arr):
    # Write your code here
    daig1, daig2 = 0,0
    for i in range(len(arr)):
        daig1 += arr[i][i]

    for j in range(len(arr)):
        daig2 += arr[j][(len(arr)-1) - j]
    return abs(daig1 - daig2)
    
    
print(diagonalDifference(map))


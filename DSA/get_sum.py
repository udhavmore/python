"""
Sum of 2 numbers from array. Do not pick the neighbour
Input: [2,3,2]
Output: 4 (2+2)

Input: [1,2,3,1]
Output: 4 (1+3, 2+1, 1+1)

Input: [5,1,3,11]
Output: 16 (5+3, 1+11, 5+11)
"""

def maximum_sum(arr):
    if arr is None or len(arr) == 0:
        return 0
    
    n = len(arr)
    pick = [0 for _ in range(n)]
    dont_pick = [0 for _ in range(n)]
    pick[0] = arr[0]
    print(f"Pick: {pick}")
    print(f"Dont Pick: {dont_pick}")

    for i in range(1, n):
        pick[i] = dont_pick[i-1] + arr[i]
        dont_pick[i] = max(dont_pick[i-1], pick[i-1])
        print(f"Pick: {pick[i]} || Don't Pick: {dont_pick[i]}")

    print(f"Pick: {pick} || Don't Pick: {dont_pick}")


print(maximum_sum([2,3,2]))
# print(maximum_sum([5,1,3,11]))

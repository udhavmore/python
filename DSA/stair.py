def staircase(stairs):
    # space = n - 2
    # for stairs in range(1, n):
    #     print(' ' * space, '#' * stairs)
    #     space -= 1
    # print('#' * n)
    for stair in range(1, stairs+1):
        spaces = stairs - stair
        print(" "*spaces, "#"*stair)

staircase(6)

def plusMinus(arr):
    divisor = len(arr)
    #  [pos, neg, zero]
    ratio = [0,0,0]
    for i in range(len(arr)):
        if arr[i] > 0:
            ratio[0] += 1
        elif arr[i] < 0:
            ratio[1] += 1
        elif arr[i] == 0:
            ratio[2] += 1    

    for x in ratio:
        print(round(x/divisor, 6))

array = [-4, 3, -9, 0, 4, 1]
plusMinus(array)
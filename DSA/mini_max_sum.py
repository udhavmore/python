def miniMaxSum(arr: list):
    sum_values = []
    # nums = arr.split(" ")
    int_array = []
    for num in arr:
        int_array.append(int(num))
    
    sum_of_array = sum(int_array)

    for i in range(len(int_array)):
        val = sum_of_array - int_array[i]
        sum_values.append(val)

    min_val, max_val = min(sum_values), max(sum_values)
    print(f"{min_val} {max_val}")



numbers = "1 2 3 4 5"
miniMaxSum(numbers)

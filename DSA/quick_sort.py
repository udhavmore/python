def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start<len(array) and array[start] <= pivot:
            start += 1
        
        while array[end] > pivot:
            end -= 1
        
        if start < end:
            array[start],  array[end] = array[end],  array[start]
        
    array[pivot_index], array[end] = array[end], array[pivot_index]
    return end

def quick_sort(array, start, end):
    if start<end:
        partition_index = partition(array, start, end)
        quick_sort(array, start, partition_index-1)
        quick_sort(array, partition_index+1, end)


if __name__=='__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
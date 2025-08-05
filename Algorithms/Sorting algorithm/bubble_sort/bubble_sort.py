def bubble_sort(arr):
    n = len(arr)
    if not arr or n == 1:
        return
    for i in range(n):
        for current_index in range(n - 1 - i):
            if arr[current_index] > arr[current_index + 1]:
                arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]
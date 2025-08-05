# Bubble sort

- Bubble sort repeatedly swaps adjacent elements if they’re out of order, pushing the largest unsorted value to the end each pass. ***Worst-case: O(n²).***

## Execution 

1. if `arr[current_index] > arr[current_index + 1]` then swap
2. after each iteration for outer loop the inner loops value will decrease to not check the already sorted indexes, `n - 1 - i`
### code

```python

def bubble_sort(arr):
    n = len(arr)
    if not arr or n == 1:
        return
    
    for i in range(n):
        for current_index in range(n - 1 - i):
            if arr[current_index] > arr[current_index + 1]:
                arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]
```
# Binary search

- Binary search is a fast way to find an item in a sorted list by repeatedly cutting the search range in half—check the middle, then search left or right depending on the value. ***Time complexity: O(log n).***
1. find `mid` of the array
2. `if target > arr[mid]` 
    - `high = mid - 1`
3. `elif target < arr[mid]`
    - `low = mid + 1`

## Equation to find `mid` and order of operation

$$
mid = low - (high - low) // 2
$$


```2 - (2 - 2) // 2 == 0```

1. Compute the difference between high and low:
    - `high - low`
2. Divide that difference by 2 (using floor division //):
    - `(high - low) // 2`
3. Subtract the result from low:
    - `low - ((high - low) // 2)`

### Code

```python
def binary_search(arr: list, target: any) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

```
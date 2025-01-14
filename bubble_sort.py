def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))  # Output: [11, 12, 22, 25, 34, 64, 90]

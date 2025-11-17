def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Test array
array = [10, 20, 30, 40, 50, 60]
target = 40

# Perform search
result = binary_search(array, target)

print("Array:", array)
print("Target:", target)
print("Index found at:", result)

def binary_search(arr, item):
    arr.sort()  # Sorting the array for binary search
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Integer division for indexing
        guess = arr[mid]

        if guess == item:
            return mid  # Return the index if found
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None  # Return None if the item is not found

arr = [1, 2, 3, 4, 5, 987, 7, 65, 4, 443, 33]
print(binary_search(arr, 3))  # Output: Index of 3 in sorted array

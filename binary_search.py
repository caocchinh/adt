# Python program for implementation of Binary Search (Iterative)

def binarySearch(arr, target):
    """
    Perform a binary search for the target in the sorted array arr.
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate mid index
        # (low + high) // 2 can overflow in some languages, 
        # though not Python, but this is the standard robust way:
        mid = low + (high - low) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not present in the array
    return -1

# Demonstration
print("=== Binary Search Demonstration ===")
arr = [2, 3, 4, 10, 40]
target = 10

print(f"Array: {arr}")
print(f"Searching for target: {target}")

result = binarySearch(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

# Test not found
target = 15
print(f"\nSearching for target: {target}")
result = binarySearch(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

# Python program for implementation of Insertion Sort

# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # 5
        j = i - 1 # 2

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            # 3 (13) = 13
            # 2 (13) = 12
            # 1 (12) = 11
            j -= 1
            # j = 1
            # = 0
            # = -1
            # [11, 12, 13, 13, 6]
            # [11, 12, 12, 13, 6]
            # [11, 11, 12, 13, 6]
        arr[j + 1] = key
        # arr[0] = 5
        # [5, 11, 12, 13, 6]

# A utility function to print array of size n 
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    arr = [11, 12, 13, 5, 6]
    insertionSort(arr)
    printArray(arr)
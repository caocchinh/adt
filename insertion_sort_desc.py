# Python program for implementation of Insertion Sort in descending order


def insertionSortDescending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def printArray(arr):
    for value in arr:
        print(value, end=" ")
    print()


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSortDescending(arr)
    printArray(arr)

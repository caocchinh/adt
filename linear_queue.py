queue = [-1] * 5
headIndex = -1
freeIndex = 0

def enQueue(value):
    global headIndex, freeIndex, queue
    if (freeIndex >= len(queue)):
        return False
    queue[freeIndex] = value
    if headIndex == -1:
        headIndex = 0
    freeIndex += 1
    return True

def countItem(start):
    global freeIndex, queue
    if (start < freeIndex):
        return queue[start] + countItem(start - 1)
    return 0

enQueue(2)
enQueue(3)
enQueue(4)
print(queue)
print(countItem(headIndex))
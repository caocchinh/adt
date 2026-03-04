queue = [None] * 5
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

def deQueue():
    global headIndex, freeIndex, queue
    if (headIndex == -1):
        return False
    queue[headIndex] = None
    headIndex += 1
    if (headIndex == freeIndex):
        headIndex = -1
        freeIndex = 0
    return True

def countItem():
    global headIndex, freeIndex
    if headIndex == -1:
        return 0
    return freeIndex - headIndex



enQueue(2)
enQueue(3)
enQueue(4)
enQueue(4)
enQueue(4)
enQueue(4)


print(queue)
print(countItem())
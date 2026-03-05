headIndex = -1
tailIndex = -1
numberOfItems = 0
queue = [-1] * 20


def enQueue(value):
    global queue, headIndex, tailIndex, numberOfItems
    if (numberOfItems >= len(queue)):
        return False
    if tailIndex == -1:
        headIndex = 0
        tailIndex = 0
        queue[0] = value
    else:
        tailIndex += 1
        if (tailIndex >= len(queue)):
            tailIndex = 0
        queue[tailIndex] = value
    numberOfItems += 1
    return True

def deQueue():
     global queue, headIndex, tailIndex, numberOfItems
     if (numberOfItems <= 0):
        return False
     returnValue = queue[headIndex]
     queue[headIndex] = -1
     headIndex += 1
     if (headIndex >= len(queue)):
        headIndex = 0
     numberOfItems -= 1
     if (numberOfItems == 0):
        headIndex = -1
        tailIndex = -1
     return returnValue

enQueue(10)
enQueue(12)
enQueue(14)


deQueue()

print(queue)
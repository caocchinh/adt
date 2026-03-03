headIndex = -1
tailIndex = -1
numberOfItems = 0
queue = [-1] * 20


def enQueue(value):
    global queue, headIndex, tailIndex
    if (numberOfItems >= len(queue)):
        return False
    if tailIndex == -1:
        headIndex = 0
        tailIndex = 0
        queue[0] = value
    else:
        tailIndex += 1
        if (tailIndex >= 20):
            tailIndex = 0
        queue[tailIndex] = value
    numberOfItems += 1
    return True

def deQueue():
     global queue, headIndex, tailIndex
     if (numberOfItems <= 0):
        return False
     returnValue = queue[headIndex]
     del queue[headIndex]
     headIndex += 1
     if (headIndex >= 20):
        headIndex = 0
     numberOfItems -= 1
     if (numberOfItems == 0):
        headIndex = -1
        tailIndex = -1
     return returnValue


# Computer Science A-level Style Stack ADT Implementation
# Uses a fixed-size array and a top pointer

stackSize = 10
stack = [None] * stackSize
topPointer = -1

def isEmpty():
    global topPointer
    return topPointer == -1

def isFull():
    global topPointer, stackSize
    return topPointer == stackSize - 1

def push(item):
    global topPointer, stack, stackSize
    if isFull():
        print("Stack Overflow! Cannot push item:", item)
        return False
    else:
        topPointer += 1
        stack[topPointer] = item
        return True

def pop():
    global topPointer, stack
    if isEmpty():
        print("Stack Underflow! Cannot pop from empty stack.")
        return None
    else:
        item = stack[topPointer]
        stack[topPointer] = None # Optional: clear the value
        topPointer -= 1
        return item

def peek():
    global topPointer, stack
    if isEmpty():
        print("Stack is empty. Nothing to peek.")
        return None
    else:
        return stack[topPointer]

def outputStack():
    global topPointer, stack
    print(f"Current Stack (topPointer: {topPointer}):")
    if isEmpty():
        print("[Empty]")
    else:
        for i in range(topPointer, -1, -1):
            print(f"[{i}]: {stack[i]}")

# Demonstration / Testing for A-level course
if __name__ == "__main__":
    print("=== Pure Stack ADT Demonstration ===")
    
    outputStack()
    
    print("\nPushing items: 5, 12, 8")
    push(5)
    push(12)
    push(8)
    outputStack()
    
    print(f"\nPeek top: {peek()}")
    
    print("\nPopping two items...")
    print(f"Popped: {pop()}")
    print(f"Popped: {pop()}")
    outputStack()
    
    print("\nPushing until full (Max size: 10)...")
    for i in range(1, 11):
        push(i * 10)
    
    outputStack()
    
    print("\nAttempting overflow push...")
    push(999)
    
    print("\nPopping everything until empty...")
    while not isEmpty():
        pop()
    
    outputStack()
    
    print("\nAttempting underflow pop...")
    pop()

    print("\n=== Demonstration Complete ===")

class node:
    def __init__(self, theData, nextNodeNumber):
        self.Data = theData
        self.nextNode = nextNodeNumber 

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),
 node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyListStartPointer = 5 

def outputNodes(start, linkedListArray):
    # Start from the beginning of the list
    current = start
    # Continue until we reach a node with nextNode = -1
    while current != -1:
        print(linkedListArray[current].Data)
        current = linkedListArray[current].nextNode

def addNodeWithData(dataToAdd):
    global emptyListStartPointer, linkedList, startPointer
    # Step 1: Validate that emptyListStartPointer points to a valid index (0-9)
    # If emptyListStartPointer is out of bounds (no free slots), return False, emptyListStartPointer
    if emptyListStartPointer < 0 or emptyListStartPointer > len(linkedList) - 1:
        return False

    # Step 2: Save the next free slot BEFORE overwriting the empty node
    oldEmptyListStartPointer = emptyListStartPointer

    # Step 2.1: Update the emptyListStartPointer to the next free slot
    emptyListStartPointer = linkedList[emptyListStartPointer].nextNode

    # Step 3: Create a new node with the input data and nextNode = -1 (end of list)
    newNode = node(dataToAdd, -1)

    # Step 4: Place the new node in the current emptyListStartPointer position
    linkedList[oldEmptyListStartPointer] = newNode

    # Step 5: Find the last node in the linked list to attach the new node
    # Traverse until we find a node whose nextNode is -1 (the tail)
    previousPointer = startPointer
    while linkedList[previousPointer].nextNode != -1:
        previousPointer = linkedList[previousPointer].nextNode

    # Step 6: Attach the new node to the end of the list
    linkedList[previousPointer].nextNode = oldEmptyListStartPointer

    # Step 7: Return success and the updated emptyList pointer
    return True

def testAddNode():
    """Test function to demonstrate addNode without user input"""
    global emptyListStartPointer
    print("=== Testing addNode function ===")
    print("Current list:")
    outputNodes(startPointer, linkedList)

    print(f"\nCurrent emptyListStartPointer: {emptyListStartPointer}")
    print("Available empty nodes chain: 5->6->8->9->-1")

    # Test adding a node with value 99
    print("\nAdding node with value 99...")
    result = addNodeWithData(99)

    if result:
        print("Node added successfully!")
        print(f"Updated emptyListStartPointer: {emptyListStartPointer}")
        print("Updated list:")
        outputNodes(startPointer, linkedList)
    else:
        print("Failed to add node - no empty slots available")

    print("\n=== Test Complete ===")

# Run the test
testAddNode()
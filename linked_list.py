class node:
    def __init__(self, theData, nextNodeNumber):
        self.Data = theData
        self.nextNode = nextNodeNumber 

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(None,6),
 node(None,8),node(56,3),node(None,9),node(None,-1)]
startPointer = 0
emptyListStartPointer = 5 

def outputNodes():
    global startPointer, linkedList
    # Start from the beginning of the list
    current = startPointer
    # Continue until we reach a node with nextNode = -1
    while current != -1:
        print(linkedList[current].Data)
        current = linkedList[current].nextNode

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

def removeNode(dataToRemove):
    global startPointer, emptyListStartPointer, linkedList
    
    # Check if the list is empty
    if startPointer == -1:
        return False
    
    # Check if the node to be removed is the first node
    if linkedList[startPointer].Data == dataToRemove:
        oldStartPointer = startPointer
        startPointer = linkedList[oldStartPointer].nextNode
        linkedList[oldStartPointer].Data = None
        linkedList[oldStartPointer].nextNode = emptyListStartPointer # Make it point to the first item in the empty list
        emptyListStartPointer = oldStartPointer # Make the empty list start at the removed node
        return True


    currentPointer = startPointer # 
    previousPointer = -1

    # Traverse the list to find the node
    while currentPointer != -1 and linkedList[currentPointer].Data != dataToRemove:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode
        
    # If the node was not found
    if currentPointer == -1:
        return False
        
    # Bypass the node to be removed, by pointing it to the next node
    linkedList[previousPointer].nextNode = linkedList[currentPointer].nextNode
    
    # Add the removed node back to the empty list
    linkedList[currentPointer].Data = None
    linkedList[currentPointer].nextNode = emptyListStartPointer # Make it point to the first item in the empty lít
    emptyListStartPointer = currentPointer # Make the empty list start at the removed node
    
    return True

def testAddNode():
    """Test function to demonstrate addNode without user input"""
    global emptyListStartPointer
    print("=== Testing addNode function ===")
    print("Current list:")
    outputNodes()

    print(f"\nCurrent emptyListStartPointer: {emptyListStartPointer}")
    print("Available empty nodes chain: 5->6->8->9->-1")

    # Test adding a node with value 99
    print("\nAdding node with value 99...")
    result = addNodeWithData(99)

    if result:
        print("Node added successfully!")
        print(f"Updated emptyListStartPointer: {emptyListStartPointer}")
        print("Updated list:")
        outputNodes()
    else:
        print("Failed to add node - no empty slots available")

    print("\n=== Test Complete ===")

def testRemoveNode():
    """Test function to demonstrate removeNode without user input"""
    global emptyListStartPointer
    print("\n=== Testing removeNode function ===")
    
    # Let's remove an existing node, e.g., value 6
    print("Attempting to remove node with value 6...")
    result = removeNode(1)
    
    if result:
        print("Node removed successfully!")
        print(f"Updated emptyListStartPointer: {emptyListStartPointer}")
        print("Updated list:")
        outputNodes()
    else:
        print("Failed to remove node")
    
    print("\n=== Test Complete ===")

# Run the tests
testAddNode()
testRemoveNode()

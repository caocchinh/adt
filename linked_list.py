class node:
    def __init__(self, theData, nextNodeNumber):
        self.Data = theData
        self.nextNode = nextNodeNumber 

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),
 node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5 

def outputNodes(start, linkedListArray):
    # Start from the beginning of the list
    current = start
    # Continue until we reach a node with nextNode = -1
    while current != -1:
        print(linkedListArray[current].Data)
        current = linkedListArray[current].nextNode

def addNodeWithData(linkedList, currentPointer, emptyList, dataToAdd):
    """Version of addNode that accepts data as parameter for testing"""

    # Step 2: Validate that emptyList points to a valid index (0-9)
    # If emptyList is out of bounds (no free slots), return False
    if emptyList < 0 or emptyList > 9:
        return False

    # Step 3: Create a new node with the input data and nextNode = -1 (end of list)
    newNode = node(dataToAdd, -1)

    # Step 4: Place the new node in the current emptyList position
    linkedList[emptyList] = newNode

    # Step 5: Find the last node in the linked list to attach the new node
    # Start from the beginning and traverse until we find a node with nextNode = -1
    previousPointer = 0  # Keep track of the previous node
    while true:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode

    # Step 6: Attach the new node to the end of the list
    # Set the last node's nextNode to point to the new node (emptyList index)
    linkedList[previousPointer].nextNode = emptyList

   
    return True

def testAddNode():
    """Test function to demonstrate addNode without user input"""
    print("=== Testing addNode function ===")
    print("Current list:")
    outputNodes(startPointer, linkedList)

    print(f"\nCurrent emptyList pointer: {emptyList}")
    print("Available empty nodes chain: 5->6->8->9->-1")

    # Test adding a node with value 99
    print("\nAdding node with value 99...")
    result = addNodeWithData(linkedList, startPointer, emptyList, 99)

    if result:
        print("Node added successfully!")
        print(f"Updated emptyList pointer: {emptyList}")
        print("Updated list:")
        outputNodes(startPointer, linkedList)
    else:
        print("Failed to add node - no empty slots available")

    print("\n=== Test Complete ===")

# Run the test
testAddNode()
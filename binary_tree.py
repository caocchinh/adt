import pprint
ArrayNodes = [[0 for _ in range(3)] for _ in range(20)]
RootPointer = -1
FreeNodeIndex = 0

def AddNodes(data):
    global ArrayNodes, RootPointer, FreeNodeIndex
    if (FreeNodeIndex < len(ArrayNodes)):
        ArrayNodes[FreeNodeIndex][0] = -1
        ArrayNodes[FreeNodeIndex][1] = data
        ArrayNodes[FreeNodeIndex][2] = -1
        if (RootPointer == -1):
            RootPointer = 0
        else:
            CurrentRootPointer = RootPointer
            isPlaced = False
            while isPlaced == False:
                if (data < ArrayNodes[CurrentRootPointer][1]):
                    if (ArrayNodes[CurrentRootPointer][0] == -1):
                        ArrayNodes[CurrentRootPointer][0] = FreeNodeIndex
                        isPlaced = True
                    else:
                        CurrentRootPointer = ArrayNodes[CurrentRootPointer][0]
                else:
                    if (ArrayNodes[CurrentRootPointer][2] == -1):
                        ArrayNodes[CurrentRootPointer][2] = FreeNodeIndex
                        isPlaced = True
                    else:
                        CurrentRootPointer = ArrayNodes[CurrentRootPointer][2]
        FreeNodeIndex += 1
    else:
        print("Tree is full")

def InOrder(RootNodeIndex):
 global ArrayNodes
 if ArrayNodes[RootNodeIndex][0] != -1:
    InOrder(ArrayNodes[RootNodeIndex][0])
 print(str(ArrayNodes[RootNodeIndex][1]))
 if ArrayNodes[RootNodeIndex][2] != -1:
    InOrder( ArrayNodes[RootNodeIndex][2])

            

AddNodes(120)
AddNodes(10)
AddNodes(12)
AddNodes(50)
AddNodes(5)
AddNodes(25)
AddNodes(150)
AddNodes(3)
AddNodes(7)
AddNodes(75)
AddNodes(30)
AddNodes(200)
AddNodes(1)
AddNodes(15)
AddNodes(40)
AddNodes(100)
AddNodes(125)
AddNodes(175)
AddNodes(250)
AddNodes(2)

InOrder(RootPointer)


# pprint.pprint(ArrayNodes)

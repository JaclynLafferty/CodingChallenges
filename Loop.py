#Class Implementation
class Node:
    data = None
    nextNode = None

    def __init__(self, d: int):
        data = d

#Solution Function
def findLoop(head: Node):
    nodesSeen = set()

    while (head != None):
        if head in nodesSeen:
            return head

        nodesSeen.add(head)
        head = head.nextNode

    return None

#Testing
firstNode= Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)
fifthNode = Node(5)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
thirdNode.nextNode = fourthNode
fourthNode.nextNode = fifthNode
fifthNode.nextNode = thirdNode

result = findLoop(firstNode)

#Address Of Object id()
if id(result) == id(thirdNode):
    print("Loop found at Node: " + str(thirdNode))

else:
    print("No loop found.")
#Class Implementation
class Node:
    data = None
    nextNode = None

    def __init__(self, d: int):
        data = d

#Solution Function
def findIntersection(head1: Node, head2: Node):
    nodesSeen = set()

    while (head1 != None):
        nodesSeen.add(head1)
        head1 = head1.nextNode

    while (head2 != None):
        if head2 in nodesSeen:
            return head2

        nodesSeen.add(head2)
        head2 = head2.nextNode

    return None

#Testing
firstNode= Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)

firstNode.nextNode = thirdNode
secondNode.nextNode = thirdNode
thirdNode.nextNode = fourthNode

result = findIntersection(firstNode, secondNode)

#Address Of Object id()
if id(result) == id(thirdNode):
    print("Intersection found at Node: " + str(thirdNode))
    
else:
    print("No intersection found.")
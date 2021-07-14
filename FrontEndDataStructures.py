class frontNode:
    alphabetOrder = 'A'
    def __init__(self,label,instructionGroup,isEndNode,hur) -> None:
        
        self.label = label
        self.instructionGroup = instructionGroup
        self.isEndNode = isEndNode
        self.hur = hur
    @classmethod
    def increaseOrder(cls):
        cls.alphabetOrder = chr(ord(cls.alphabetOrder) + 1)
    @classmethod
    def resetOrder(cls):
        cls.alphabetOrder = 'A'

class Edge:
    def __init__(self,cost:int,costLabel,instructionGroup) -> None:
        self.cost = cost
        self.costLabel = costLabel
        self.instructionGroup = instructionGroup
        

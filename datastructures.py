class Node:
    def __init__(self,xPos,yPos,identfier,size,isEnd,hur,parent = None) -> None:
        self.xPos = xPos 
        self.yPos = yPos
        self.identfier = identfier
        self.isEnd = isEnd
        self.size = size
        self.hur = hur
        self.parent = parent
        

class Graph:
    def __init__(self,Nodes) -> None:
        self.adj_list = {}
        self.nodes = Nodes
        for node in self.nodes:
            self.adj_list[node.identfier] = []
    
    def getNode(self,identfier):
        for node in self.nodes:
            if node.identfier == identfier:
                return node
        return None

    def getNodeNextList(self , identifier):
        for node in self.nodes:
            if node.identfier == identifier:
                return self.adj_list[node.identfier]
        return None

    def addEdges(self,Edges):
        for edge in Edges:
            From,to,cost = edge 
            self.addSingleEdge(From,to,cost)

    def addSingleEdge(self,From,to,cost = 0 ):
        self.adj_list[From].append((to,cost))

    def printGraph(self):
        for node in self.nodes:
            print(node.identfier,":",self.adj_list[node.identfier])

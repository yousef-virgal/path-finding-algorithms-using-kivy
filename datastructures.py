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

if __name__ == "__main__":
    nodes = [Node(1,1,"1",1,False,0),Node(2,2,"2",1,False,0),Node(3,3,"3",1,False,0),Node(4,4,"4",1,False,0)]
    Edges = [("1","2",3),("1","3",6),("2","4",5),("1","4",9)]
    graph = Graph(nodes)
    graph.addEdges(Edges)
    print(graph.getNodeNextList("1"))
    print(type(graph.dfs))
    graph.printGraph()
    print('\n\n\n')
    print(type(graph.DFS))

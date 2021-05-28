from datastructures import Graph as MyGraph
from datastructures import Node as Node
class PathFinding():
    def __init__(self,graphP, heuristic) -> None:
        self.graph = graphP
        self.heuristic = heuristic
    def checkGoal(self,node):
        return node.isEnd
    def BFS(self,startNode):
        visited = []
        non_visited = [startNode]
        path = []
        while len(non_visited) != 0:
            victim = non_visited.pop()
            path.append(victim.identfier)
            if self.checkGoal(victim):
                print("3aaaaaaaaaaaaaaaaaaa GOAL IS ")
                print(victim.identfier)
                print('Path ->')
                print(path)
                return
            if(type(victim) is Node):
                visited.append(victim)
                afterVictimList = self.graph.getNodeNextList(victim.identfier)
                print("Victim -> ")
                print(victim.identfier)
                print("After victim list ->")
                print(afterVictimList)

                for i in afterVictimList:
                    non_visited.insert(0,self.graph.getNode(i[0][0]))

        return
    def DFS(self,startNode):
        visited = []
        non_visited = [startNode]
        path = []
        while len(non_visited) != 0:
            victim = non_visited.pop(0)
            path.append(victim.identfier)
            if self.checkGoal(victim):
                print("3aaaaaaaaaaaaaaaaaaa GOAL IS ")
                print(victim.identfier)
                print('Path ->')
                print(path)
                return
            if(type(victim) is Node):
                visited.append(victim)
                afterVictimList = self.graph.getNodeNextList(victim.identfier)
                print("Victim -> ")
                print(victim.identfier)
                print("After victim list ->")
                print(afterVictimList)
                print(reversed(afterVictimList))

                for i in reversed(afterVictimList):
                    non_visited.insert(0,self.graph.getNode(i[0][0]))
        return
    def greedy(self,startNode):
        visited = []
        non_visited = [startNode]
        path = []
        while(len(non_visited) != 0 ):
             victim = non_visited.pop(0)
             path.append(victim.identfier)
             if self.checkGoal(victim):
                 return
             if(type(victim) is Node):
                visited.append(victim)
                afterVictimList = self.graph.getNodeNextList(victim.identfier)
                print("Victim -> ")
                print(victim.identfier)
                print("After victim list ->")
                print(afterVictimList)






if __name__ == "__main__":
    n1 = Node(1,1,'A',1,False,1)
    n2 = Node(1,2,'B',1,False,1)
    n3 = Node(1,3,'C',1,False,1,1)
    n4 = Node(1,4,'D',1,False,1,1)
    n5 = Node(1,5,'E',1,False,1,1)
    n6 = Node(1,4,'F',1,False,1,1)
    n7 = Node(1,4,'G',1,True,1,1)
    
    nodes = [n1,n2,n3,n4,n5,n6,n7]
    edges = [('A','B',1),('A','C',1),('B','D',1),('B','E',1),('C','F',1),('C','G',1)]

    g = MyGraph(nodes)
    g.addEdges(edges)
    g.printGraph()
    p = PathFinding(g,1)
    print("NODE WITH IDENTIFIER A: ")

    p.DFS(g.getNode('A'))



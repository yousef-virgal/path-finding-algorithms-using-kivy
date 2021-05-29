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
                print(type(afterVictimList[0]))
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
    def ucs(self,startNode):
            visited = []
            non_visited = [{startNode:startNode.identfier, 'cost':0}]
            path = []
            while len(non_visited) != 0:
                victim = non_visited.pop(0)
                print('victim ->')
                print(victim)
                victimDict = victim
                print('victimDict ->')
                print(victimDict)
                cost = victimDict.get('cost')
                for i in victimDict.items() :
                    print(i)
                    victim = i[0]
                    break
                
                path.append({victim.identfier:cost})
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
                    print(type(afterVictimList))
                    print(afterVictimList)

                    for i in afterVictimList:
                        print('Esm el node \n i[0][0]')
                        print(i[0])
                        print(' cost bta3ha i[1] ->')
                        print(i[1])
                        print(cost)
                        non_visited.append({self.graph.getNode(i[0][0]):self.graph.getNode(i[0][0]).identfier,'cost':(i[1] + cost)})
                    print(non_visited)
                    #Sorting non_visited by values 
                    non_visited = sorted(non_visited, key = lambda kv:kv['cost'])
                    print('non visited ya beh')
                    print(non_visited)

                    

            return
    def astar(self,startNode):
                visited = []
                non_visited = [{startNode:startNode.identfier, 'cost':0}]
                path = []
                while len(non_visited) != 0:
                    victimDict = non_visited.pop(0)
                    print('\n')
                    print('victimDict ->')
                    print(victimDict)
                    cost = victimDict.get('cost')
                    print(cost)
                    print('\n')
                    for i in victimDict.items():
                        print(i)
                        victim = i[0]
                        print(victim)
                        break
                    

                    
                    path.append({victim.identfier:cost})
                    if self.checkGoal(victim):
                        
                        print(path)
                        return
                    if(cost != 0):    
                        cost = cost - victim.hur
                    if(type(victim) is Node):
                        visited.append(victim)
                        afterVictimList = self.graph.getNodeNextList(victim.identfier)
                        

                        for i in afterVictimList:
                            
                            #cost =  cost - victim.hur
                            print('heuristichaaa')
                            print(self.graph.getNode(i[0]).hur)
                            non_visited.append({self.graph.getNode(i[0][0]):self.graph.getNode(i[0][0]).identfier,'cost':(i[1] + cost +self.graph.getNode(i[0]).hur )})
                        print(non_visited)
                        #Sorting non_visited by values 
                        non_visited = sorted(non_visited, key = lambda kv:kv['cost'])
                        print('non visited ya beh')
                        print(non_visited)
                        temp = []
                        
                

                        

                return







if __name__ == "__main__":
    n1 = Node(1,1,'A',1,False,5)
    n2 = Node(1,2,'B',1,False,4)
    n3 = Node(1,3,'C',1,False,2,1)
    n4 = Node(1,4,'D',1,False,6,1)
    n5 = Node(1,5,'E',1,False,8,1)
    n6 = Node(1,4,'F',1,False,2,1)
    n7 = Node(1,4,'G',1,True,0,1)
    n8 = Node(1,4,'S',1,False,3,1)
    n9 = Node(1,4,'H',1,False,4,1)
    n10 = Node(1,4,'I',1,False,9,1)
    
    
    nodes = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
    edges = [('A','S',1),('A','G',10),('S','C',1),('S','B',2),('B','D',5),('C','D',3),('C','G',4),('D','G',0)]

    g = MyGraph(nodes)
    g.addEdges(edges)
    g.printGraph()
    p = PathFinding(g,1)
    print("NODE WITH IDENTIFIER A: ")

    p.astar(g.getNode('A'))



import queue
import time
import threading
from kivy.graphics import InstructionGroup

class Algorthims:
    
    def __init__(self,graph,startNode,window) -> None:
        self.graph = graph
        self.startNode = startNode
        self.window = window
    def BFS(self):
        visited = []
        queue = []
        queue.append(self.startNode)
        visited.append(self.startNode)
        while queue:

            item = queue.pop(0)
            node = self.graph.getNode(item)
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(0.1)
            lock.release()
            
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(0.1)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return

            for neghbour in self.graph.adj_list[item]:
                if neghbour[0] not in visited:
                    self.graph.getNode(neghbour[0]).parent = node
                    queue.append(neghbour[0])
                    visited.append(neghbour[0])
    def DFS(self):
        visited = []
        non_visited = [self.startNode]

        while non_visited:
            victim = non_visited.pop(0)
            visited.append(victim)

            node = self.graph.getNode(victim)
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(0.1)
            lock.release()
            
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(0.1)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()

                return
            
            afterVictimList = self.graph.adj_list[victim]

            for i in reversed(afterVictimList):
                if i[0] not in visited:
                    self.graph.getNode(i[0]).parent = node
                    non_visited.insert(0,i[0])
        return

    def ucs(self):
            visited = []
            myStartNode = self.graph.getNode(self.startNode)
            non_visited = [{myStartNode:myStartNode.identfier, 'cost':0}]

            while non_visited:
                victim = non_visited.pop(0)
                visited.append(victim)
                victimDict = victim
                cost = victimDict.get('cost')

                for i in victimDict.items() :
                    victim = i[0]
                    break
                
                lock = threading.Lock()
                lock.acquire()
                node = self.graph.getNode(victim.identfier)
                self.window.drawYellow(node)
                time.sleep(0.1)
                lock.release()

                if node.isEnd:
                    currentNode = node
                    while currentNode.parent != None:
                        lock.acquire()
                        self.window.drawPurple(currentNode)
                        
                        self.window.changeLineColor(currentNode.parent,currentNode)
                        time.sleep(0.1)
                        lock.release()
                        currentNode = currentNode.parent

                    lock.acquire()
                    self.window.drawPurple(currentNode)
                    lock.release()
                    return
                
                
                afterVictimList = self.graph.getNodeNextList(victim.identfier)

                for i in afterVictimList:
                    if i[0] not in visited:
                        self.graph.getNode(i[0]).parent = node
                        non_visited.append({self.graph.getNode(i[0][0]):self.graph.getNode(i[0][0]).identfier,'cost':(i[1] + cost)})
                        #Sorting non_visited by values 
                        non_visited = sorted(non_visited, key = lambda kv:kv['cost'])
            return
    def IDS(self,maxDepth = 10):

        for i in range(maxDepth):
            if self.DS(i):
                return
    def DS(self,i):

        visited = []
        queue = []
        queue.append((self.startNode,0))
        visited.append(self.startNode)
        
        while queue:

            item = queue.pop(0)
            node = self.graph.getNode(item[0])
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(0.1)
            lock.release()

            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(0.1)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return True

            for neghbour in self.graph.adj_list[item[0]]:
                if neghbour[0] not in visited and item[1]<= i:
                    self.graph.getNode(neghbour[0]).parent = node
                    count = item[1]+1
                    queue.append((neghbour[0],count))
                    visited.append(neghbour[0])
        self.window.resetColors()
        return False
    def astar(self):
        
            visited = []
            myStartNode = self.graph.getNode(self.startNode)
            non_visited = [{myStartNode:myStartNode.identfier, 'cost':0}]
            path = []
            while len(non_visited) != 0:
                victim = non_visited.pop(0)
                victimDict = victim
                cost = victimDict.get('cost')
                for i in victimDict.items():
                    print(i)
                    victim = i[0]
                    print(victim)
                    break
                lock = threading.Lock()
                lock.acquire()
                node = self.graph.getNode(victim.identfier)
                self.window.drawYellow(node)
                time.sleep(0.1)
                lock.release()
                path.append({victim.identfier:cost})
                if node.isEnd:
                    currentNode = node
                    while currentNode.parent != None:
                        lock.acquire()
                        self.window.drawPurple(currentNode)
                            
                        self.window.changeLineColor(currentNode.parent,currentNode)
                        time.sleep(0.1)
                        lock.release()
                        currentNode = currentNode.parent

                    lock.acquire()
                    self.window.drawPurple(currentNode)
                    lock.release()
        
                    print(path)
                    return
                if(cost != 0):    
                    cost = cost - victim.hur
                visited.append(victim)
                afterVictimList = self.graph.getNodeNextList(victim.identfier)
                        

                for i in afterVictimList:
                    if i[0] not in visited:
                        self.graph.getNode(i[0]).parent = node
                        non_visited.append({self.graph.getNode(i[0][0]):self.graph.getNode(i[0][0]).identfier,'cost':(i[1] + cost +self.graph.getNode(i[0]).hur )})
                        print(non_visited)
                #Sorting non_visited by values 
                non_visited = sorted(non_visited, key = lambda kv:kv['cost'])
            return
    def greedy(self):
        visited = []
        myStartNode = self.graph.getNode(self.startNode)
        non_visited = [{myStartNode:myStartNode.identfier, 'cost':0}]
        path = []
        while len(non_visited) != 0:
            victim = non_visited.pop(0)
            victimDict = victim
            cost = victimDict.get('cost')
            for i in victimDict.items() :
                print(i)
                victim = i[0]
                break
                
            lock = threading.Lock()
            lock.acquire()
            node = self.graph.getNode(victim.identfier)
            self.window.drawYellow(node)
            time.sleep(0.1)
            lock.release()
            path.append({victim.identfier:cost})
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                        
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(0.1)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return
                
            visited.append(victim)
            afterVictimList = self.graph.getNodeNextList(victim.identfier)

            for i in afterVictimList:
                if i[0] not in visited:
                    self.graph.getNode(i[0]).parent = node
                    non_visited.append({self.graph.getNode(i[0][0]):self.graph.getNode(i[0][0]).identfier,'cost':(self.graph.getNode(i[0]).hur )})

                #Sorting non_visited by values 
            non_visited = sorted(non_visited, key = lambda kv:kv['cost'])
            print('non visited ya beh')
            print(non_visited)
        return    
                    

import queue
import time
import threading
from kivy.graphics import InstructionGroup
from queue import PriorityQueue

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
            time.sleep(self.window.speed*1.5/100)
            lock.release()
            
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
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
            time.sleep(self.window.speed*1.5/100)
            lock.release()
            
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
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
        queue = PriorityQueue()
        count = 1
        queue.put((0,self.startNode))
        while queue:
            item = queue.get()
            visited.append(item[1])
            node = self.graph.getNode(item[1])
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(self.window.speed*1.5/100)
            lock.release()
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return
            
            for i in self.graph.adj_list[item[1]]:
                if i[0] not in visited:
                    
                    self.graph.getNode(i[0]).parent = node
                    visited.append(i[0])
                    queue.put((item[0]+i[1],i[0]))    
                        
            count += 1
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
            time.sleep(self.window.speed*1.5/100)
            lock.release()

            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
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
        queue = PriorityQueue()
        queue.put((self.graph.getNode(self.startNode).hur+0,self.startNode,0))
        while queue:
            item = queue.get()
            visited.append(item[1])
            node = self.graph.getNode(item[1])
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(self.window.speed*1.5/100)
            lock.release()
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return
            
            for i in self.graph.adj_list[item[1]]:
                if i[0] not in visited:             
                    self.graph.getNode(i[0]).parent = node
                    visited.append(i[0])
                    queue.put((self.graph.getNode(i[0]).hur+item[2]+i[1],i[0],item[2]+i[1]))
            print(queue.queue)

    
    def greedy(self):
        visited = []
        queue = PriorityQueue()
        queue.put((self.graph.getNode(self.startNode).hur,self.startNode))
        while queue:
            item = queue.get()
            visited.append(item[1])
            node = self.graph.getNode(item[1])
            lock = threading.Lock()
            lock.acquire()
            self.window.drawYellow(node)
            time.sleep(self.window.speed*1.5/100)
            lock.release()
            if node.isEnd:
                currentNode = node
                while currentNode.parent != None:
                    lock.acquire()
                    self.window.drawPurple(currentNode)
                     
                    self.window.changeLineColor(currentNode.parent,currentNode)
                    time.sleep(self.window.speed*1.5/100)
                    lock.release()
                    currentNode = currentNode.parent

                lock.acquire()
                self.window.drawPurple(currentNode)
                lock.release()
                return
            
            for i in self.graph.adj_list[item[1]]:
                if i[0] not in visited:             
                    self.graph.getNode(i[0]).parent = node
                    visited.append(i[0])
                    queue.put((self.graph.getNode(i[0]).hur,i[0]))
                           

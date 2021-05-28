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

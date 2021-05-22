import time
from kivy.graphics import InstructionGroup,Ellipse,Color
import threading
class Algorthims:
    def __init__(self,graph,startNode,window) -> None:
        self.graph = graph
        self.startNode = startNode
        self.window = window
    
    def update(self,instance):
        print("tis is being called")
        for key in self.circleDict:
            self.window.ids.canvasID.canvas.remove(self.circleDict[key])
            self.window.ids.canvasID.canvas.add(self.circleDict[key])

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
                return
            for neghbour in self.graph.adj_list[item]:
                if neghbour not in visited:
                    queue.append(neghbour[0])
                    visited.append(neghbour[0])

from logging import root
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder, builder
from kivy.graphics import Ellipse,Color,Line,InstructionGroup,Rectangle
from datastructures import Node,Graph
from arrow import *
from algo import Algorthims 
from kivy.animation import Animation
import math
import  time
import threading
from enum import Enum

RADIUS:int = 22
class Types(Enum):
    BFS = 1
    DFS = 2
    UCS = 3
    GREDY = 4
    ASTAR = 5
    #add more ?
    

class MyBoxLayout(Widget):

    toggleButtons:list = []    
    alphabetOrder = 'A'
    #dictionary contains all the labels letters as keys and label objects as values to add  them to the canvas
    LabelDict:dict = {}
    #dictionary contains all the labels letters as keys and Instruction group as values to be able to remove circlies and re-draw them
    circleDict:dict = {}
    # nested dictionary contains label letters to rpresent from and to nodes
    graph:dict = {}
    # contains the index of the first node that was clicked when adding an edge
    firstNode = None
    #counter for the number of times a click occured  when adding an edge should only take values between 1 and 2
    count:int = 1
    # variable indicating if a node is a start node or not
    startNode:bool = True
    algoType:Types = Types.BFS # added 
    #coust = ObjectProperty(None)

    #Constructor -->
    def __init__(self, **kwargs)->None:
        super().__init__(**kwargs)
        self.toggleButtons = [self.ids.node_button, self.ids.clearButtonID, self.ids.rightArrowID]
        


    def makeAllButtonsUp(self,savedbutton)->None:
        for i in self.toggleButtons:
            if i == savedbutton:
                continue
            else:
                i.state = 'normal'

            
    def animate_button(self,widget):
        pass

    def spinner_clicked(self,value):
        pass
    


    #convert the dictionary to node list object should be called before creating the graph and passing the result to the graph object
    def convertNodesToList(self)->list:
        list = []
        for key in self.LabelDict:
            xPos = self.LabelDict[key][0].x
            yPos = self.LabelDict[key][0].y 
            isEnd = self.LabelDict[key][1]
            hur = self.LabelDict[key][2]
            list.append(Node(xPos,yPos,key,RADIUS,isEnd,hur))
        return list 
    
    def convertEdges(self)->list:
        edges:list = []
        for firstKey in self.graph:
            for secondKey in self.graph[firstKey]:
                edges.append((firstKey,secondKey,self.graph[firstKey][secondKey][1]))
        return edges


    def drawYellow(self,node:Node)->None:

        self.obj = InstructionGroup()
        self.obj.add(Color(1,1,0,1,mode="rgba"))
        self.obj.add(Ellipse(pos=(node.xPos,node.yPos),size = (node.size*2,node.size*2)))
        self.ids.canvasID.canvas.remove(self.circleDict[node.identfier])
        self.circleDict[node.identfier] = self.obj
        self.ids.canvasID.canvas.add(self.obj)
    
    def drawPurple(self,node:Node)->None:

        self.obj = InstructionGroup()
        self.obj.add(Color(128.0/255.0,0,128.0/255.0,1,mode="rgba"))
        self.obj.add(Ellipse(pos=(node.xPos,node.yPos),size = (node.size*2,node.size*2)))
        self.ids.canvasID.canvas.remove(self.circleDict[node.identfier])
        self.circleDict[node.identfier] = self.obj
        self.ids.canvasID.canvas.add(self.obj)

    def changeLineColor(self,first,second):
        if isinstance(self.graph['A'][list(self.graph['A'].keys())[0]][0],InstructionGroup):
            self.obj = InstructionGroup()
            self.obj.add(Color(1,69.0/255.0,0,1,mode="rgba"))
            self.obj.add(Line(points=[first.xPos+RADIUS, first.yPos+RADIUS,
            second.xPos+RADIUS, second.yPos+RADIUS],width = 2))
            self.ids.canvasID.canvas.add(self.obj)

            #self.graph[first.identfier][second.identfier][0] = self.obj

            firstLabel = self.LabelDict[first.identfier][0]
            secondLabel = self.LabelDict[second.identfier][0]  
            item1 = self.circleDict[first.identfier]
            item2  = self.circleDict[second.identfier]

            self.remove_widget(firstLabel)
            self.remove_widget(secondLabel)
            self.ids.canvasID.canvas.remove(item1)
            self.ids.canvasID.canvas.remove(item2)
        #adding part
            self.ids.canvasID.canvas.add(item1)
            self.ids.canvasID.canvas.add(item2)
            self.add_widget(firstLabel)
            self.add_widget(secondLabel)
        else:
            self.graph[first.identfier][second.identfier][0].main_color = [1,69.0/255.0,0,1]
    # draws a node on to the screen
    def drawNode(self,touch):
        # inillize an instruction group for this node
        self.obj = InstructionGroup()
        #variable to track if its an end node
        endNode = False
        # first node inserted should be the start node
        #if condtions to check if right clicked and set the color acordingly
        if self.startNode:
            self.obj.add(Color(0,1,0,1,mode="rgba"))
            self.startNode = False
        elif touch.button == 'right':
            self.obj.add(Color(0,0,1,1,mode = "rgba"))
            endNode = True
        else:
            self.obj.add(Color(rgb=(1,0,0)))
        #adds the ellipse and draws on to the canvas
        self.obj.add(Ellipse(pos=(touch.x-RADIUS,touch.y-RADIUS),size=(RADIUS*2,RADIUS*2)))
        self.ids.canvasID.canvas.add(self.obj)
        
        
        hur = 0# should be taken from textbox



        #adds the label and adds it to widgets
        l = Label(text= self.alphabetOrder, pos = [touch.x-RADIUS,touch.y-RADIUS],font_size = 15,color = (0,0,0,1),
        size = (RADIUS*2,RADIUS*2),pos_hint = (1,1),size_hint=(0.2,0.2))
        self.add_widget(l)
        #adds the label and instruction groups to the dictionaries
        self.LabelDict[self.alphabetOrder] = (l,endNode, hur)
        self.circleDict[self.alphabetOrder] = self.obj
        self.graph[self.alphabetOrder] = {}
        #incrments the letter
        self.alphabetOrder = chr(ord(self.alphabetOrder) + 1)



    #deletes a node from th screen
    def clearNode(self,x,y)->None:
        #loop through the label dictionary cheking if the x and y postion from the touch lay in the boundries of one of them
        for key in self.LabelDict:
                    if x > self.LabelDict[key][0].x and y > self.LabelDict[key][0].y and x < self.LabelDict[key][0].x+RADIUS*2 and y<self.LabelDict[key][0].y+RADIUS*2:
                        #delete a all edges pointing from this node to other nodes


                        for secondKey in self.graph[key]:
                            if isinstance(self.graph[key][secondKey][0],InstructionGroup):
                                self.ids.canvasID.canvas.remove(self.graph[key][secondKey][0])
                            else:
                                self.remove_widget(self.graph[key][secondKey][0])
                        self.graph.pop(key)
                        

                        #delete all edges pointing to this node
                        for firstKey in self.graph:
                            for secondKey in self.graph[firstKey]:
                                if secondKey == key:
                                    if isinstance(self.graph[firstKey][secondKey][0],InstructionGroup):
                                        self.ids.canvasID.canvas.remove(self.graph[firstKey].pop(secondKey)[0])
                                    else:
                                        test = self.graph[firstKey][secondKey][0]
                                        self.remove_widget(test)
                                    break
                        
                        #delete the label
                        l = self.LabelDict.pop(key)
                        item = self.circleDict.pop(key)
                        self.remove_widget(l[0])
                        self.ids.canvasID.canvas.remove(item)
                        break
    

    def solve(self):

        graph = Graph(self.convertNodesToList())
        graph.addEdges(self.convertEdges())
        algo = Algorthims(graph,'A',self)
        thread = threading.Thread(target = algo.BFS)
        thread.start()

    # clears the whole screen
    def clearStuff(self):

        #loops through all the labels and removes them
        for key in self.LabelDict:
            self.remove_widget(self.LabelDict[key][0])
        self.ids.canvasID.canvas.clear()
        
        for firstKey in self.graph:
            for secondKey in self.graph[firstKey]:
                if isinstance(self.graph[firstKey][secondKey][0],Arrow):
                    self.remove_widget(self.graph[firstKey][secondKey][0])

        #resets variables to thier intiall condition 
        self.LabelDict = {}
        self.circleDict = {}
        self.alphabetOrder = 'A'
        self.graph = {}
        self.startNode = True
        # redraws the actuall board
        with self.ids.canvasID.canvas:
            Color(1,1,1,1, mode = 'rgba')
            Rectangle(size = self.ids.canvasID.size,pos = self.ids.canvasID.pos)

    


    def on_touch_up(self, touch):
        # check if the touch lies in the canvas to draw in
        if(touch.y < self.ids.canvasID.size[1] and touch.y > RADIUS + 20 and touch.x> RADIUS + 20 and touch.x<self.ids.canvasID.size[0]-RADIUS):

            # check the state of toogle buttons
            if(self.ids.node_button.state == 'down'):
                self.drawNode(touch)
                return

            elif self.ids.doubleArrowID.state == 'down':

                for key in self.LabelDict:
                        if touch.x > self.LabelDict[key][0].x and touch.y > self.LabelDict[key][0].y and touch.x < self.LabelDict[key][0].x +RADIUS*2 and touch.y<self.LabelDict[key][0].y+RADIUS*2:
                            if self.count == 2: 

                                self.count  = 1
                                self.obj = InstructionGroup()
                                self.obj.add(Color(0,0,0,1,mode='rgba'))
                                self.obj.add(Line(points=[self.LabelDict[self.firstNode][0].x+RADIUS, self.LabelDict[self.firstNode][0].y+RADIUS,
                                self.LabelDict[key][0].x +RADIUS, self.LabelDict[key][0].y+RADIUS],width = 2))


                                cost = 0
                            
                                self.graph[self.firstNode][key] = (self.obj,cost)
                                self.graph[key][self.firstNode] = (self.obj,cost)
                                
                                self.ids.canvasID.canvas.add(self.obj)

                                firstLabel = self.LabelDict[key][0]
                                secondLabel = self.LabelDict[self.firstNode][0]

                                #triger a redraw of the 2 nodes by removing them and then adding them again
                                item1 = self.circleDict[key]
                                item2  = self.circleDict[self.firstNode]

                                self.remove_widget(firstLabel)
                                self.remove_widget(secondLabel)
                                self.ids.canvasID.canvas.remove(item1)
                                self.ids.canvasID.canvas.remove(item2)
                                #adding part
                                self.ids.canvasID.canvas.add(item1)
                                self.ids.canvasID.canvas.add(item2)
                                self.add_widget(firstLabel)
                                self.add_widget(secondLabel)
                                self.startNode = None
                                return 
                            else:
                                self.count += 1
                                self.firstNode = key
                                return 
                return

            #draws an edge
            elif(self.ids.rightArrowID.state == 'down'):
                for key in self.LabelDict:
                        if touch.x > self.LabelDict[key][0].x and touch.y > self.LabelDict[key][0].y and touch.x < self.LabelDict[key][0].x +RADIUS*2 and touch.y<self.LabelDict[key][0].y+RADIUS*2:
                            if self.count == 2:  
                                self.count  = 1

                                vx = self.LabelDict[key][0].x+RADIUS-(self.LabelDict[self.firstNode][0].x+RADIUS)
                                vy = self.LabelDict[key][0].y+RADIUS-(self.LabelDict[self.firstNode][0].y+RADIUS)
                                distance = math.sqrt(((vx)**2)+((vy)**2))
                                ax =(self.LabelDict[self.firstNode][0].x+RADIUS) + vx /distance * RADIUS 
                                ay = (self.LabelDict[self.firstNode][0].y+RADIUS) + vy /distance * RADIUS

                                self.arrow = Arrow(main_color = [0,0,0,0.8],o_x = ax, o_y = ay,
                                fletching_radius = 0, head_angle= 30, to_x = self.LabelDict[key][0].x+RADIUS, to_y = self.LabelDict[key][0].y+RADIUS, shaft_width = 2,outline_color = [1,1,1,1],
                                distance = distance-2*RADIUS )

                                cost = 0 #update with textbox
                                
                                self.graph[self.firstNode][key] = (self.arrow,cost)
                                
                                self.add_widget(self.arrow)

                                
                                self.startNode = None
                                return 
                            else:
                                self.count += 1
                                self.firstNode = key
                                return 
                return 

            elif(self.ids.clearButtonID.state == 'down'):
                self.clearNode(touch.x,touch.y)
                return
                #delete Node
                
                
class MainWindow(App):
    def build(self):
       return MyBoxLayout()


if __name__ == '__main__':
    MainWindow().run()
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('kivy','window_icon','wireless-connectivity.png')
from kivy.core.window import Window
Window.size = (1200,600)
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse,Color,Line,InstructionGroup,Rectangle
from datastructures import Node,Graph
from arrow import *
from algo import Algorthims 
import math
import threading
from kivy.uix.popup import Popup
from Constants import *
from FrontEndDataStructures import *

class  MyPopup(Popup):
    def fxport(self):
        app = App.get_running_app()
        app.fileBeforeName=self.ids.filechooser.path
        app.fileNameOnly = self.ids.chooserName.text
        app.filePath = app.fileBeforeName + '\\' + app.fileNameOnly

class MyBoxLayout(Widget):
    #List of toggle buttons on the system
    toggleButtons:list = []  
    #observer for spinner value intially no algorithm is selected
    spinnerChoice:str = 'Algorithm'  
    #alphabetOrder = 'A'
    #dictionary contains all the labels letters as keys and label objects as values to add  them to the canvas
    LabelDict:dict = {}
    # nested dictionary contains label letters to rpresent from and to nodes
    graph:dict = {}
    # contains the index of the first node that was clicked when adding an edge
    firstNode = None
    #counter for the number of times a click occured  when adding an edge should only take values between 1 and 2
    count:int = 1
    # Flags
    startNode:bool = True
    algoType:Types = Types.BFS # added 
    heurFlag = False
    cost_right_flag = False
    cost_double_flag = False
    EnterMaxLevelFlag = False
    firstFlag = False
    speed = 20

    #Constructor -->
    def __init__(self, **kwargs)->None:
        super().__init__(**kwargs)
        self.toggleButtons = [self.ids.node_button, self.ids.clearButtonID, self.ids.rightArrowID,self.ids.doubleArrowID]
        
        
    def changePathLabel(self):
        app = App.get_running_app()
        self.ids.pathLabel.text = app.fileBeforeName
    def saveButton(self):
        app = App.get_running_app()
        self.export_to_png(app.filePath)


    def updateValue(self,*args):
        self.speed = args[1]
    
    def setAlgorithmType(self,spinnerValue):
        #"A*","Greedy","Breadth first search","Depth first search","Uniformed cost search"]
        if(spinnerValue == "Breadth first search"):
            self.algoType = Types.BFS
        elif(spinnerValue == "Depth first search"):
            self.algoType = Types.DFS
        elif(spinnerValue == "Uniformed cost search"):
            self.algoType = Types.UCS
        elif(spinnerValue == "A*"):
            self.algoType = Types.ASTAR
        elif(spinnerValue == "Greedy"):
            self.algoType = Types.GREDY
        elif(spinnerValue == "IDS"):
            if(self.EnterMaxLevelFlag == False):
                #self.ids.textBoxID.text = "Enter Max level"
                self.EnterMaxLevelFlag = True
            self.algoType = Types.IDS
        return

    def deleteDraw(self):
        for first in self.graph:
            for second in self.graph[first]:
                if isinstance(self.graph[first][second].instructionGroup,InstructionGroup):
                    self.ids.canvasID.canvas.remove(self.graph[first][second].instructionGroup)
                    self.obj = InstructionGroup()
                    self.obj.add(Color(0,0,0,1,mode='rgba'))
                    self.obj.add(Line(points=[self.LabelDict[first].label.x+RADIUS, self.LabelDict[first].label.y+RADIUS,
                    self.LabelDict[second].label.x +RADIUS, self.LabelDict[second].label.y+RADIUS],width = 2))
                    self.ids.canvasID.canvas.add(self.obj)
                    self.graph[first][second].instructionGroup = self.obj
                else:
                    self.graph[first][second].instructionGroup.main_color = [0,0,0,0.8]        
        self.resetColors()
        
    def makeAllButtonsUp(self,savedbutton)->None:
        for i in self.toggleButtons:
            if i == savedbutton:
                continue
            else:
                i.state = 'normal'

    def spinner_clicked(self,value):
        self.spinnerChoice = value
        if value == 'IDS' and self.EnterMaxLevelFlag == False:
            self.ids.textBoxID.text = 'Enter Max Level '
            self.EnterMaxLevelFlag = True
#convert the dictionary to node list object should be called before creating the graph and passing the result to the graph object
    def convertNodesToList(self)->list:
        list = []
        for key in self.LabelDict:
            xPos = self.LabelDict[key].label.x
            yPos = self.LabelDict[key].label.y 
            isEnd = self.LabelDict[key].isEndNode
            hur = self.LabelDict[key].hur
            list.append(Node(xPos,yPos,key,RADIUS,isEnd,hur))
        return list 
    
    def convertEdges(self)->list:
        edges:list = []
        for firstKey in self.graph:
            for secondKey in self.graph[firstKey]:
                edges.append((firstKey,secondKey,self.graph[firstKey][secondKey].cost))
        return edges

    def drawColor(self,node:Node,color:str)->None:
        self.obj = InstructionGroup()
        if color == 'Yellow':
            self.obj.add(Color(1,1,0,1,mode="rgba"))
        elif color == 'Purple':
            self.obj.add(Color(128.0/255.0,0,128.0/255.0,1,mode="rgba"))
        self.obj.add(Ellipse(pos=(node.xPos,node.yPos),size = (node.size*2,node.size*2)))
        self.ids.canvasID.canvas.remove(self.LabelDict[node.identfier].instructionGroup)
        self.LabelDict[node.identfier].instructionGroup = self.obj
        self.ids.canvasID.canvas.add(self.obj)
    
    def changeLineColor(self,first,second):
        if isinstance(self.graph['A'][list(self.graph['A'].keys())[0]].instructionGroup,InstructionGroup):
            self.obj = InstructionGroup()
            self.obj.add(Color(1,69.0/255.0,0,1,mode="rgba"))
            self.obj.add(Line(points=[first.xPos+RADIUS, first.yPos+RADIUS,
            second.xPos+RADIUS, second.yPos+RADIUS],width = 2))
            self.ids.canvasID.canvas.add(self.obj)
            self.graph[first.identfier][second.identfier].instructionGroup = self.obj #may be deleted
            self.remove_widget(self.LabelDict[first.identfier].label)
            self.remove_widget(self.LabelDict[second.identfier].label)
            self.ids.canvasID.canvas.remove(self.LabelDict[first.identfier].instructionGroup)
            self.ids.canvasID.canvas.remove(self.LabelDict[second.identfier].instructionGroup)
        #adding part
            self.ids.canvasID.canvas.add(self.LabelDict[first.identfier].instructionGroup)
            self.ids.canvasID.canvas.add(self.LabelDict[second.identfier].instructionGroup)
            self.add_widget(self.LabelDict[first.identfier].label)
            self.add_widget(self.LabelDict[second.identfier].label)
        else:
            self.graph[first.identfier][second.identfier].instructionGroup.main_color = [1,69.0/255.0,0,1]

    def resetColors(self):
        for circle in self.LabelDict:
            self.remove_widget(self.LabelDict[circle].label)
            self.ids.canvasID.canvas.remove(self.LabelDict[circle].instructionGroup)
            self.obj = InstructionGroup()
            if circle == 'A':
                self.obj.add(Color(rgb=(0,1,0)))
            elif self.LabelDict[circle].isEndNode:
                self.obj.add(Color(rgb=(0,0,1)))
            else:
                self.obj.add(Color(rgb=(1,0,0)))
            self.obj.add(Ellipse(pos=(self.LabelDict[circle].label.x,self.LabelDict[circle].label.y),size=(RADIUS*2,RADIUS*2)))
            self.LabelDict[circle].instructionGroup = self.obj
            self.ids.canvasID.canvas.add(self.obj)   
            l = Label(text= "{}\n{}".format(str(circle),self.LabelDict[circle].hur), pos = [self.LabelDict[circle].label.x,self.LabelDict[circle].label.y],font_size = 15,color = (0,0,0,1),
            size = (RADIUS*2,RADIUS*2),pos_hint = (1,1),size_hint=(0.2,0.2))
            self.add_widget(l)
            self.LabelDict[circle].label = l
    # draws a node on to the screen
    def drawNode(self,touch):
        hur = 0
        if self.ids.textBoxID.text.isnumeric():
            hur = int(self.ids.textBoxID.text)

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
        #adds the label and adds it to widgets
        l = Label(text= frontNode.alphabetOrder+"\n{}".format(hur), pos = [touch.x-RADIUS,touch.y-RADIUS],font_size = 15,color = (0,0,0,1),
        size = (RADIUS*2,RADIUS*2),pos_hint = (1,1),size_hint=(0.2,0.2))
        self.add_widget(l)
        #adds the label and instruction groups to the dictionaries
        self.LabelDict[frontNode.alphabetOrder] = frontNode(label=l,isEndNode=endNode,instructionGroup=self.obj,hur = hur)
        #self.circleDict[self.alphabetOrder] = self.obj
        self.graph[frontNode.alphabetOrder] = {}
        #incrments the letter
        frontNode.increaseOrder()
    #deletes a node from th screen
    def clearNode(self,x,y)->None:
        #loop through the label dictionary cheking if the x and y postion from the touch lay in the boundries of one of them
        for key in self.LabelDict:
            if x > self.LabelDict[key].label.x and y > self.LabelDict[key].label.y and x < self.LabelDict[key].label.x+RADIUS*2 and y<self.LabelDict[key].label.y+RADIUS*2:
                #delete a all edges pointing from this node to other nodes
                for secondKey in self.graph[key]:
                    if isinstance(self.graph[key][secondKey].instructionGroup,InstructionGroup):
                        self.ids.canvasID.canvas.remove(self.graph[key][secondKey].instructionGroup)
                    else:
                        self.remove_widget(self.graph[key][secondKey].instructionGroup)
                    self.remove_widget(self.graph[key][secondKey].costLabel)
                self.graph.pop(key)    
                        #delete all edges pointing to this node
                for firstKey in self.graph:
                    for secondKey in self.graph[firstKey]:
                        if secondKey == key:
                            if isinstance(self.graph[firstKey][secondKey].instructionGroup,InstructionGroup):
                                self.ids.canvasID.canvas.remove(self.graph[firstKey][secondKey].instructionGroup)
                            else:
                                self.remove_widget(self.graph[firstKey][secondKey].instructionGroup)
                            self.remove_widget(self.graph[firstKey][secondKey].costLabel)
                            self.graph[firstKey].pop(secondKey)
                            break
                        
                #delete the label
                l = self.LabelDict.pop(key)
                self.remove_widget(l.label)
                self.ids.canvasID.canvas.remove(l.instructionGroup)
                break
    

    def solve(self):
        graph = Graph(self.convertNodesToList())
        graph.addEdges(self.convertEdges())
        algo = Algorthims(graph,'A',self)
        self.setAlgorithmType(self.spinnerChoice)
        self.deleteDraw()
        if(self.algoType == Types.BFS):
            thread = threading.Thread(target = algo.BFS)
        elif(self.algoType == Types.DFS):
            thread = threading.Thread(target = algo.DFS)
        elif(self.algoType == Types.UCS):
            thread = threading.Thread(target = algo.ucs)
        elif(self.algoType == Types.ASTAR):
            thread = threading.Thread(target = algo.astar)
        elif(self.algoType == Types.GREDY):
            thread = threading.Thread(target = algo.greedy)
        elif(self.algoType == Types.IDS):
            if self.ids.textBoxID.text.isnumeric():
                maxDepth = int(self.ids.textBoxID.text)
            else:
                maxDepth = 10
            thread = threading.Thread(target = algo.IDS, args= (maxDepth,))
        else:
            return

        #thread = threading.Thread(target = self.setAlgorithmType(spinnerValue= self.spinnerChoice))
        thread.start()
    # clears the whole screen
    def clearStuff(self):
        #loops through all the labels and removes them
        for key in self.LabelDict:
            self.remove_widget(self.LabelDict[key].label)
        self.ids.canvasID.canvas.clear()
        for firstKey in self.graph:
            for secondKey in self.graph[firstKey]:
                if isinstance(self.graph[firstKey][secondKey].instructionGroup,Arrow):
                    self.remove_widget(self.graph[firstKey][secondKey].instructionGroup)
                self.remove_widget(self.graph[firstKey][secondKey].costLabel)
        #resets variables to thier intiall condition 
        self.LabelDict = {}
        frontNode.resetOrder()
        self.graph = {}
        self.startNode = True
        # redraws the actuall board
        with self.ids.canvasID.canvas:
            Color(1,1,1,1, mode = 'rgba')
            Rectangle(size = self.ids.canvasID.size,pos = self.ids.canvasID.pos)
   
    def calculateMidpoint(self,firstNode:str,secondNode:str):
        point1 = [self.LabelDict[firstNode].label.x+RADIUS , self.LabelDict[firstNode].label.y+RADIUS]
        point2 = [self.LabelDict[secondNode].label.x +RADIUS , self.LabelDict[secondNode].label.y+RADIUS]
        slope = (self.LabelDict[secondNode].label.y+RADIUS - self.LabelDict[firstNode].label.y-RADIUS)/(self.LabelDict[secondNode].label.x +RADIUS - self.LabelDict[firstNode].label.x-RADIUS)
        if slope/abs(slope) == 1:
            midPoint = [((point1[0]+point2[0])/2) ,((point1[1]+point2[1])/2) +12.5 ]
        else:
            midPoint = [((point1[0]+point2[0])/2) +5 ,((point1[1]+point2[1])/2)  ]
        return midPoint
    def drawEdge(self,touch,type:str):
        for key in self.LabelDict:
            if touch.x > self.LabelDict[key].label.x and touch.y > self.LabelDict[key].label.y and touch.x < self.LabelDict[key].label.x +(RADIUS*2) and touch.y<self.LabelDict[key].label.y+(RADIUS*2):
                if key == self.firstNode:
                    return
                if self.count == 2: 
                    self.count  = 1
                    if type == 'Double':
                        self.obj = InstructionGroup()
                        self.obj.add(Color(0,0,0,1,mode='rgba'))
                        self.obj.add(Line(points=[self.LabelDict[self.firstNode].label.x+RADIUS, self.LabelDict[self.firstNode].label.y+RADIUS,
                        self.LabelDict[key].label.x +RADIUS, self.LabelDict[key].label.y+RADIUS],width = 2))
                    else:
                        vx = (self.LabelDict[key].label.x+RADIUS)-(self.LabelDict[self.firstNode].label.x+RADIUS)
                        vy = (self.LabelDict[key].label.y+RADIUS)-(self.LabelDict[self.firstNode].label.y+RADIUS)
                        distance = math.sqrt(((vx)**2)+((vy)**2))
                        ax =(self.LabelDict[self.firstNode].label.x+RADIUS) + (vx /distance) * RADIUS 
                        ay = (self.LabelDict[self.firstNode].label.y+RADIUS) + (vy /distance) * RADIUS
                        self.arrow = Arrow(main_color = [0,0,0,0.8],o_x = ax, o_y = ay,
                        fletching_radius = 0, head_angle= 30, to_x = self.LabelDict[key].label.x+RADIUS, to_y = self.LabelDict[key].label.y+RADIUS, shaft_width = 2,outline_color = [1,1,1,1],
                        distance = distance-2*RADIUS )

                    cost = 0 
                    if self.ids.textBoxID.text.isnumeric():
                        cost = int(self.ids.textBoxID.text)
                    costLabel = Label(text = str(cost),pos = self.calculateMidpoint(self.firstNode,key),font_size = '20sp', size = (10,10) , color = [1,0,0,1])
                    self.add_widget(costLabel)
                    if type == 'Double':      
                        self.graph[self.firstNode][key] = Edge(cost=cost,costLabel=costLabel,instructionGroup=self.obj)
                        self.graph[key][self.firstNode] = Edge(cost=cost,costLabel=costLabel,instructionGroup=self.obj)
                        self.ids.canvasID.canvas.add(self.obj)
                        firstLabel = self.LabelDict[key].label
                        secondLabel = self.LabelDict[self.firstNode].label
                        #triger a redraw of the 2 nodes by removing them and then adding them again
                        item1 = self.LabelDict[key].instructionGroup
                        item2  = self.LabelDict[self.firstNode].instructionGroup
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
                        self.graph[self.firstNode][key] = Edge(cost=cost,costLabel=costLabel,instructionGroup=self.arrow)               
                        self.add_widget(self.arrow)
                    self.firstNode = None
                    return
                else:
                    self.count += 1
                    self.firstNode = key
                    return                
    def checkInatialState(self):
        if(self.ids.node_button.state == 'down' and self.heurFlag == False ):
            self.ids.textBoxID.text = "Enter heuristic"
            self.heurFlag = True
        elif (self.ids.doubleArrowID.state == 'down' and self.cost_double_flag == False) :
            self.ids.textBoxID.text = "Enter cost"
            self.cost_double_flag = True
        elif(self.ids.rightArrowID.state == 'down' and self.cost_right_flag == False):
            self.ids.textBoxID.text = "Enter cost"
            self.cost_right_flag = True
    def on_touch_up(self, touch):
        self.checkInatialState()
        if(touch.y < self.ids.canvasID.size[1] and touch.y > RADIUS + 20 and touch.x> RADIUS + 20 and touch.x<self.ids.canvasID.size[0]-RADIUS):
            if(self.ids.node_button.state == 'down'):
                self.drawNode(touch)
                return
            elif self.ids.doubleArrowID.state == 'down':
                self.drawEdge(touch=touch,type='Double')
                return
            elif(self.ids.rightArrowID.state == 'down'):
                self.drawEdge(touch=touch,type='Single') 
                return 
            elif(self.ids.clearButtonID.state == 'down'):
                self.clearNode(touch.x,touch.y)
                return
            
class MainWindow(App):
    fileBeforeName:str =''
    fileNameOnly:str =''
    filePathX:str = ''
    def build(self):
        self.title = 'Path-Finding Algorithms'
        return MyBoxLayout()
       
if __name__ == '__main__':
    MainWindow().run()
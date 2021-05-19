from logging import root
from typing import Final
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder, builder
from kivy.graphics import Ellipse,Color,Line,InstructionGroup,Rectangle
from math import sqrt

RADIUS = 15


class MyBoxLayout(Widget):
    alphabetOrder = 'A'
    LabelDict = {}
    circleDict = {}
    graph = {}
    firstNode = None
    count = 1

    def spinner_clicked(self,value):
        pass

    def drawNode(self,x,y):
        self.obj = InstructionGroup()
        self.obj.add(Color(rgb=(1,0,0)))
        self.obj.add(Ellipse(pos=(x-RADIUS,y-RADIUS),size=(RADIUS*2,RADIUS*2)))
        self.ids.canvasID.canvas.add(self.obj)
        l = Label(text= self.alphabetOrder, pos = [x-RADIUS,y-RADIUS],font_size = 15,color = (0,0,0,1),
        size = (RADIUS*2,RADIUS*2),pos_hint = (1,1),size_hint=(0.2,0.2))
        self.LabelDict[self.alphabetOrder] = l
        self.circleDict[self.alphabetOrder] = self.obj
        self.add_widget(l)
        self.graph[self.alphabetOrder] = {}
        self.alphabetOrder = chr(ord(self.alphabetOrder) + 1)

    def clearNode(self,x,y):
        for key in self.LabelDict:
                    if x > self.LabelDict[key].x and y > self.LabelDict[key].y and x < self.LabelDict[key].x+RADIUS*2 and y<self.LabelDict[key].y+RADIUS*2:
                        l = self.LabelDict.pop(key)
                        item = self.circleDict.pop(key)
                        self.remove_widget(l)
                        self.ids.canvasID.canvas.remove(item)
                        break
    
    
    def clearStuff(self):
        for key in self.LabelDict:
            self.remove_widget(self.LabelDict[key])
        self.ids.canvasID.canvas.clear()
        self.LabelDict = {}
        self.circleDict = {}
        self.alphabetOrder = 'A'
        self.graph = {}
        
        with self.ids.canvasID.canvas:
            Color(1,1,1,1, mode = 'rgba')
            Rectangle(size = self.ids.canvasID.size,pos = self.ids.canvasID.pos)

    
    def on_touch_up(self, touch):

        if(touch.y < self.ids.canvasID.size[1] and touch.y > RADIUS + 20 and touch.x> RADIUS + 20 and touch.x<self.ids.canvasID.size[0]-RADIUS):

            if(self.ids.node_button.state == 'down'):

                self.drawNode(touch.x,touch.y)
                #create a new Node
                return

            elif(self.ids.rightArrowID.state == 'down'):
                for key in self.LabelDict:
                        if touch.x > self.LabelDict[key].x and touch.y > self.LabelDict[key].pos[1] and touch.x < self.LabelDict[key].pos[0]+RADIUS*2 and touch.y<self.LabelDict[key].pos[1]+RADIUS*2:
                            if self.count == 2:  
                                self.count  = 1
                                self.obj = InstructionGroup()
                                self.obj.add(Color(0,0,0,1,mode='rgba'))
                                self.obj.add(Line(points=[self.LabelDict[self.firstNode].x+RADIUS, self.LabelDict[self.firstNode].y+RADIUS,
                                self.LabelDict[key].x +RADIUS, self.LabelDict[key].y+RADIUS],width = 3))
                                self.graph[self.firstNode][key] = self.obj
                                self.ids.canvasID.canvas.add(self.obj)

                                firstLabel = self.LabelDict[key]
                                secondLabel = self.LabelDict[self.firstNode]

                                item1 = self.circleDict[key]
                                item2  = self.circleDict[self.firstNode]
                                self.remove_widget(firstLabel)
                                self.remove_widget(secondLabel)
                                self.ids.canvasID.canvas.remove(item1)
                                self.ids.canvasID.canvas.remove(item2)

                                self.ids.canvasID.canvas.add(item1)
                                self.ids.canvasID.canvas.add(item2)
                                self.add_widget(firstLabel)
                                self.add_widget(secondLabel)
                                
    
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
                
                
class mohsenApp(App):
    def build(self):
       return MyBoxLayout()


if __name__ == '__main__':
    mohsenApp().run()
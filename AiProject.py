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
    def spinner_clicked(self,value):
        pass

    def clearStuff(self):
        for key in self.LabelDict:
            self.remove_widget(self.LabelDict[key])
        self.ids.canvasID.canvas.clear()
        self.LabelDict = {}
        self.circleDict = {}
        self.alphabetOrder = 'A'
        with self.ids.canvasID.canvas:
            Color(1,1,1,1, mode = 'rgba')
            Rectangle(size = self.ids.canvasID.size,pos = self.ids.canvasID.pos)

    
    def on_touch_up(self, touch):

        if(touch.y < self.ids.canvasID.size[1] and touch.y > RADIUS + 20 and touch.x> RADIUS + 20 and touch.x<self.ids.canvasID.size[0]-RADIUS):

            if(self.ids.node_button.state == 'down'):

                self.obj = InstructionGroup()
                self.obj.add(Color(rgb=(1,0,0)))
                self.obj.add(Ellipse(pos=(touch.x-RADIUS,touch.y-RADIUS),size=(RADIUS*2,RADIUS*2)))
                self.ids.canvasID.canvas.add(self.obj)
                l = Label(text= self.alphabetOrder, pos = [touch.x-RADIUS,touch.y-RADIUS],font_size = 15,color = (0,0,0,1),
                size = (RADIUS*2,RADIUS*2),pos_hint = (1,1),size_hint=(0.2,0.2))
                self.LabelDict[self.alphabetOrder] = l
                self.circleDict[self.alphabetOrder] = self.obj
                self.alphabetOrder = chr(ord(self.alphabetOrder) + 1)
                self.add_widget(l)
                #create a new Node
                return

            elif(self.ids.rightArrowID.state == 'down'):
                with self.ids.canvasID.canvas:
                    self.canvas.add(Color(rgb=(0,0,0)))
                    myLine = Line()
                    print(self.nodes)
                    return

            elif(self.ids.clearButtonID.state == 'down'):
                for key in self.LabelDict:
                    if touch.x > self.LabelDict[key].x and touch.y > self.LabelDict[key].pos[1] and touch.x < self.LabelDict[key].pos[0]+60 and touch.y<self.LabelDict[key].pos[1]+60:
                        l = self.LabelDict.pop(key)
                        item = self.circleDict.pop(key)
                        self.remove_widget(l)
                        self.ids.canvasID.canvas.remove(item)
                        break
                return
                #delete Node
                
                
class mohsenApp(App):
    def build(self):
       return MyBoxLayout()


if __name__ == '__main__':
    mohsenApp().run()
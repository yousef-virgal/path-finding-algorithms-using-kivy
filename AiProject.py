from logging import root
from typing import Final
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder, builder
from kivy.graphics import Ellipse,Color,Line
from math import sqrt




class MyBoxLayout(Widget):
    alphabetOrder = 'A'
    circleLabelList = []
    def spinner_clicked(self,value):
        pass
    def clearButton(self):
        self.canvas.clear()
    def drawCircle(self,x,y,diameter):
        myEllipse = Ellipse(pos=(x,y),size=(diameter,diameter))
        self.canvas.add(myEllipse)



    
    
    def on_touch_up(self, touch):
        if(touch.y < self.size[1]*0.75):
            if(self.ids.node_button.state == 'down'):
                with self.ids.canvasID.canvas:
                    self.canvas.add(Color(rgb=(1,0,0)))
                    myEllipse = Ellipse(pos=(touch.x-30,touch.y-30),size=(60,60))
                    l = Label(text= self.alphabetOrder, pos= [touch.x-30,touch.y-30],font_size=32,color= (0,0,0,1),
                    size = (60,60),pos_hint = (1,1),size_hint=(0.2,0.2))
                    
                    self.alphabetOrder = chr(ord(self.alphabetOrder) + 1)
                    self.canvas.add(myEllipse)
                    self.add_widget(l)
                    self.circleLabelList.append([myEllipse,l])
                    print(self.circleLabelList)
                    return
            if(self.ids.rightArrowID.state == 'down'):
                with self.ids.canvasID.canvas:
                    self.canvas.add(Color(rgb=(0,0,0)))
                    myLine = Line()
                    print(self.nodes)
                    return
            if(self.ids.clearButtonID.state == 'down'):
                for i in self.circleLabelList:
                    print('IN FOR LOOP.... \n\n\n')
                    print(self.circleLabelList)
                    print(i)
                    touchPoint = [touch.x,touch.y]
                    print('touch x = {} \n touch y = {} \n'.format(touchPoint[0],touchPoint[1]))
                    nodeCenter = [i[0].pos[0],i[0].pos[1]]
                    print('center x = {} \n center y = {} \n'.format(nodeCenter[0],nodeCenter[1]))
                    magnitude = sqrt((touchPoint[0]-nodeCenter[0])**2 + (touchPoint[1]-nodeCenter[1])**2)
                    print(magnitude)
                    if(magnitude<50):
                        #i[0].pos = (-1000000000,-100000000)
                        print(i[1])
                        self.remove_widget(self.circleLabelList[0][1])
                        self.canvas.ask_update()
                        self.canvas.remove(i[0])
                        
                        
                        
                        #self.drawCircle(nodeCenter[0],nodeCenter[1],60)
                        
                        
                
                


                    
                    
                    return
    
    

class mohsenApp(App):
    def build(self):
       return MyBoxLayout()


if __name__ == '__main__':
    mohsenApp().run()
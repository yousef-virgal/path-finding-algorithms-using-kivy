import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.graphics import Line
from Node import Node 


BLACK = Color(0 , 0, 0, mode = "rgba") #Barrier
WHITE = Color(255, 255, 255, mode = "rgba") #Empty
GRAY = Color(128, 128, 128, mode = "rgba") #Grid Lines
RED = Color(255, 0 , 0, mode = "rgba") #Closed
GREEN = Color(0, 255, 0, mode = "rgba") #Open
ORANGE = Color(255, 165, 0, mode = "rgba") #Start
PURPLE = Color(128, 0 , 128, mode = "rgba") #End
TURQUOISE = Color(64, 224, 208, mode = "rgba") #Path

class drawLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(drawLayout,self).__init__(**kwargs)
        self.ROWS = 20
        self.grid = []
        self.markedNodes = []
        self.isFirst =True
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()
         

    def makeGrid(self):
        gapX = self.size[0]//self.ROWS
        gapY = self.size[1]//self.ROWS
    
        for i in range(self.ROWS):
            self.grid.append([])
            for j in range(self.ROWS):
                self.grid[i].append(Node(gapX,gapY,j,i,self))

    def update(self, *args):
        self.canvas.clear()
        self.resetStuff()
        self.drawGrid(self.ROWS,self.size)
    
    def resetStuff(self):
        self.canvas.clear()
        self.isFirst = True
        self.grid = []
        self.drawGrid(self.ROWS,self.size)

    def on_touch_down(self, touch):
        if touch.y<(self.size[1]):
            if self.isFirst:
                self.makeGrid()
                self.isFirst = False
            gapX = self.size[0]//self.ROWS
            gapY = self.size[1]//self.ROWS
            row =int( touch.y//gapY)
            col = int(touch.x//gapX)
            self.grid[row][col].draw(BLACK)


        

    def drawGrid(self,rows,width):
        gapX = width[0]//rows
        gapY = width[1]//rows 
        for i in range(rows):
            with self.canvas:
                Color(0,0,0,1,mode="rgba")
                self.line = Line(points=[0,gapY*i,width[0],gapY*i],width = 1)
            for j in range(rows):
                with self.canvas:
                    Color(0,0,0,1,mode="rgba")
                    self.line = Line(points=[gapX*j,0,gapX*j,width[1]],width = 1)



class subLayout(GridLayout):
    def __init__(self,drawLayout, **kwargs):
        super(subLayout,self).__init__(**kwargs)
        self.rows = 1
        self.drawLayout = drawLayout
        self.solveButton = Button(text = "solve", size_hint = (0.2,0.2))
        self.add_widget(self.solveButton)
        self.resetButton = Button(text = "reset",size_hint = (0.2,0.2))
        self.add_widget(self.resetButton)
        self.size_hint = (.2,.2)

        self.resetButton.bind(on_press = self.clearWindow)

    def clearWindow(self,instance):
        self.drawLayout.resetStuff()




class mainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainLayout,self).__init__(**kwargs)
        Window.clearcolor = (1,1,1,1)
        self.rows = 2
        self.drawLayout = drawLayout()
        self.subLayout = subLayout(self.drawLayout)
        self.add_widget(self.subLayout)
        self.add_widget(self.drawLayout)



class main(App):
    def build(self):
        return mainLayout() 

if __name__ == "__main__":
    main().run()
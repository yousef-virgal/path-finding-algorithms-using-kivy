from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import Canvas



class Node:
    def __init__(self,widthX,widthY,row,col,win) -> None:
        self.row = row
        self.col = col
        self.widthX = widthX
        self.widthY = widthY
        self.x = widthX*row
        self.y = widthY*col
        self.color = None
        self.neighbours = []
        self.win = win

    def draw(self,color):
        with self.win.canvas:
            color
            Rectangle(pos=(self.x,self.y), size=(self.widthX,self.widthY))
    def update(self,widthX,widthY):
        self.widthX = widthX
        self.widthY = widthY
        self.x = widthX*self.row
        self.y = widthY*self.col
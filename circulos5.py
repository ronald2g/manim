from manim import *

class Diagonal(Scene):
    def construct(self):
        v=Circle(color=RED).move_to(LEFT)
        w=Circle(color=GREEN).move_to(LEFT *2+UP)
        x=Circle(color=BLUE).move_to(LEFT *3+UP*2)
        y=Circle(color=YELLOW).move_to(LEFT *4+UP*3)
        self.add(v,w,x,y)
        

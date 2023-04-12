from manim import *

class Centro(Scene):
    def construct(self):
        s=Circle(radius=2.0,color=RED)
        t=Circle(radius=1.0,color=BLUE)
        self.add(s,t)
        

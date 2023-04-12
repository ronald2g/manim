from manim import *

class Linea(Scene):
    def construct(self):
        p=Circle(color=RED).move_to(LEFT)
        q=Circle(color=GREEN).move_to(LEFT *2)
        r=Circle(color=BLUE).move_to(LEFT *3)
        s=Circle(color=YELLOW).move_to(LEFT *4)
        self.add(p,q,r,s)
        

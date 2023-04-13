from manim import *

class Circulos(Scene):
    def construct(self):
        a=Circle().move_to(UP)
        b=Circle().move_to(RIGHT)
        c=Circle().move_to(DOWN)
        d=Circle().move_to(LEFT)
        self.add(a,b,c,d)
        

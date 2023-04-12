from manim import *




class Prueba(Scene):
    def construct(self):
        c=Circle(radius=2.0,color='#FFFFFF')
        d=Circle(radius=1.0,color='#FF0000')
        self.add(c,d)
        

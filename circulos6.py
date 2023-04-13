from manim import *

class Ejemplo1(Scene):
    def construct(self):
        circulo1 = Circle(color=RED)
        circulo2 = Circle(color=GREEN).shift(LEFT*0.5)
        circulo3 = Circle(color=YELLOW).shift(LEFT*0.5+UP*0.5)
        circulo4 = Circle(color=BLUE).shift(UP*0.5)
        self.add(circulo1,circulo2,circulo3,circulo4)

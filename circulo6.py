from manim import *

class Ejemplo1(Scene):
    def construct(self):
        circulo1 = Circle(color=RED)
        circulo2 = Circle(color=GREEN).shift(LEFT*3)
        circulo3 = Circle(color=YELLOW).shift(UP*2)
        self.add(circulo1,circulo2,circulo3)

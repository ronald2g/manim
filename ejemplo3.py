from manim import *

class Ejemplo2(Scene):
    def construct(self):
        circulo1 = Circle(2.0)
        cuadrado = Circle(color=GREEN)
        self.add(circulo1,cuadrado)
        
        
        

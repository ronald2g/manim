from manim import *

class Esquinas(Scene):
    def construct(self):
        h=Circle().move_to(UR)
        i=Circle().move_to(UL)
        j=Circle().move_to(DR)
        k=Circle().move_to(DL)
        self.add(h,i,j,k)
        

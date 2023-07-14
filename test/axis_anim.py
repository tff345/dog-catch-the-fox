from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def my_text(self, content):
        return MarkupText(content, font_size=20)
    
    
    def construct(self):
        ax = Axes(x_range=(-0.5, 7), 
                  y_range=(0, 5),
                  x_length=9,
                  y_length=4, 
                  axis_config={
                      'include_ticks' : False
                      }).move_to((-1, -1, 0))
        dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
        dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
        mrk_d = self.my_text("D").next_to(dot_dog, UR)
        mrk_f = self.my_text("F").next_to(dot_fox, UR)
        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) ## Arrow(start=UP, end=DOWN, tip_length=0.35, max_stroke_width_to_length_ratio=2.5).scale(0.8)
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) ## Arrow(start=LEFT, end=RIGHT, tip_length=0.35, max_stroke_width_to_length_ratio=2.5).scale(0.8)
        mrk_v1 = self.my_text("v<sub>1</sub>").next_to(arrow_f, DOWN)
        mrk_v2 = self.my_text("v<sub>2</sub>").next_to(arrow_d, LEFT)
        
        group = VGroup(dot_fox, dot_dog, mrk_f, mrk_d, arrow_f, mrk_v1, arrow_d, mrk_v2)

        self.play(Write(ax))
        self.play(Write(group))

        


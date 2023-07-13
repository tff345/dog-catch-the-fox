from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def construct(self):
        ax = Axes(x_range=(-0.5, 7), 
                  y_range=(0, 5),
                  x_length=9,
                  y_length=4, 
                  axis_config={}).move_to((-1, -1, 0))
        dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
        dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
        mrk_d = Text("D", font_size=20).next_to(dot_dog, direction=np.array([1.,1.,0.]))
        mrk_f = Text("F", font_size=20).next_to(dot_fox, direction=np.array([1.,1.,0.]))
        arrow_d = Arrow(start=UP, end=DOWN, tip_length=0.35, max_stroke_width_to_length_ratio=2.5).scale(0.8).next_to(dot_dog, np.array([-1.,0.,0.]))
        arrow_f = Arrow(start=LEFT, end=RIGHT, tip_length=0.35, max_stroke_width_to_length_ratio=2.5).scale(0.8).next_to(dot_fox, DOWN)
        mrk_v1 = MarkupText("v<sub>1</sub>", font_size=20).next_to(arrow_f, DOWN)
        mrk_v2 = MarkupText("v<sub>2</sub>", font_size=20).next_to(arrow_d, LEFT)
        group = VGroup(dot_fox, dot_dog, mrk_f, mrk_d, arrow_f, mrk_v1, arrow_d, mrk_v2)

        self.play(Write(ax))
        self.play(Write(group))
        


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
        group = VGroup(dot_dog, dot_fox, mrk_d, mrk_f)

        self.play(Write(ax))
        self.play(Write(group))
        


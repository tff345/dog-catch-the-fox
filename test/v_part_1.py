from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def construct(self):
        question =  MarkupText(self.txt.txt['1_1'] + "\n" + self.txt.txt['1_2'], justify=True, font_size=24)
        group = VGroup(question)
        group.shift(UP*3)
        ax = Axes(x_range=(-0.5, 7), 
                  y_range=(0, 5),
                  x_length=9,
                  y_length=4)
        ax.shift(DOWN*0.8)

        self.play(Write(group), run_time=4)
        self.play(Write(ax))
        self.wait(2)
        self.play(FadeOut(group))
        self.wait()


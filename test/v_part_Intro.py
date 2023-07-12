from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def construct(self):
        title =  MarkupText(self.txt.txt['title'], justify=True, font_size=40, color=BLUE_C)
        group = VGroup(title)
        group.shift(UP*3)

        self.play(Write(group), run_time=2)
        self.wait(2)
        self.play(FadeOut(group))
        self.wait()


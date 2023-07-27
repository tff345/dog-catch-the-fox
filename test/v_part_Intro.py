from manim import *

class Tst(Scene):
    def construct(self):
        title = Title(r"猎犬追狐问题",color=GOLD,tex_template=TexTemplateLibrary.ctex)

        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait()


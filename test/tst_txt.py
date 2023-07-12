from manim import *
from source_text import TxtLib

class Tst(Scene):
    def construct(self):
        example_text = Tex(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = MathTex(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        txt = TxtLib()
        question =  MarkupText(txt.txt_1_1 + "\n" + txt.txt_1_2, justify=True, font_size=20)
        group = VGroup(question, example_text, example_tex)
        group.arrange(DOWN)
        

        self.play(Write(question), run_time=4)
        self.wait(2)
        
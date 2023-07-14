from manim import *
from source_text import TxtLib
from v_part_1 import V_P1

class Tst2(V_P1):
    v_p1 = Tst()
    def my_text(self, content):
        return MarkupText(content, font_size=20)

    def construct(self):
        fig_1 = VGroup(self.ax,self.curv1,self.grp_d,self.grp_d1,self.grp_f,self.grp_f1,self.self.a_value,self.var_q,self.br,self.a,self.dsd_line)
        self.play(FadeIn(fig_1))
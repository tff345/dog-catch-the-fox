from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def my_text(self, content):
        return MarkupText(content, font_size=20)
    
    
    def construct(self):
        ax = Axes(x_range=(-0.5, 3), 
                  y_range=(0, 3),
                  x_length=7,
                  y_length=3, 
                  axis_config={
                      'include_ticks' : False
                      }).move_to((-1, -1, 0))
        dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
        dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
        dot_d1 = Dot(ax.coords_to_point(0.5, 0.446), color=GRAY_BROWN)
        dot_f1 = Dot(ax.coords_to_point(0.79, 0), color=ORANGE)

        mrk_d = self.my_text("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = self.my_text("D<sub>1</sub>").next_to(dot_d1, UP*0.6)
        mrk_f = self.my_text("F").next_to(dot_fox, UL*0.6)
        mrk_f1= self.my_text("F<sub>1</sub>").next_to(dot_f1, DOWN*0.6)

        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = self.my_text("v<sub>1</sub>").next_to(arrow_f, DOWN)
        mrk_v2 = self.my_text("v<sub>2</sub>").next_to(arrow_d, LEFT)

        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
        dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = Tex(r"$\theta$", font_size=24).next_to(a, LEFT*0.6)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        var_q = self.my_text("q").next_to(br, UR*0.2)
        
        grp_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
        grp_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
        grp_d1 = VGroup(dot_d1,mrk_d1)
        grp_f1 = VGroup(dot_f1, mrk_f1)
        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,a_value,var_q,br,a,dsd_line)

        self.add(fig_1)
        


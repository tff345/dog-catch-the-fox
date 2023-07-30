from manim import *

class Tst(Scene):
    def my_text(self, content):
        return MarkupText(content, font_size=20)
    
    def construct(self):
        def mytex(content):
            return MathTex(content,font_size=36)
    
        ax = Axes(x_range=(-0.5, 3), 
                  y_range=(0, 3),
                  x_length=7,
                  y_length=3,
                  axis_config={
                      'include_ticks' : False,
                      'tip_shape': StealthTip
                      }).move_to((-1, -1, 0))
       
        self.play(Create(ax))
        dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
        dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
        dot_d1 = Dot(ax.coords_to_point(0.5, 0.446), color=GRAY_BROWN)
        dot_f1 = Dot(ax.coords_to_point(0.79, 0), color=ORANGE)
        mrk_d = mytex("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = mytex("D_1").next_to(dot_d1, UP*0.6)
        mrk_f = mytex("F").next_to(dot_fox, UL*0.6)
        mrk_f1= mytex("F_1").next_to(dot_f1, DOWN*0.6)
        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = mytex("v_1").next_to(arrow_f, DOWN)
        mrk_v2 = mytex("v_2").next_to(arrow_d, LEFT)
        dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        # anim_1
        grp_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
        grp_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
        grp_d1 = VGroup(dot_d1,mrk_d1)
        grp_f1 = VGroup(dot_f1, mrk_f1)
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = MathTex(r"\theta", font_size=26).next_to(a, LEFT*0.6)
        grp_ang = VGroup(a,a_value)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        br_txt = br.get_tex('q')
        grp_q = VGroup(br, br_txt)
        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], stroke_width=2.5,use_vectorized=True)
        
        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
        framebox = SurroundingRectangle(fig_1, buff =.3)
        
        self.play(Create(fig_1))
        self.play(Write(curv1))
        self.play(Create(framebox))
        self.play(FadeOut(framebox))
        self.wait()

        


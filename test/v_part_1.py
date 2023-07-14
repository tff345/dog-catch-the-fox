from manim import *
from source_text import TxtLib

class V_P1(Scene):
    txt = TxtLib()
    def my_text(self, content):
        return MarkupText(content, font_size=26)
    
    def my_tex(self, content):
        return Tex(content, font_size=36)


    def construct(self):
        # v_part_1:
        # show question
        question =  self.my_text(self.txt.txt['1_1'] + "\n" + 
                               "\n" + self.txt.txt['1_2'])
        grp_txt_1 = VGroup(question)
        grp_txt_1.shift(UP*3)
        # draw the figure
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
        # show the simulated curve
        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
        # add parameters
        dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = Tex(r"$\theta$", font_size=26).next_to(a, LEFT*0.6)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        distance_q = self.my_text("q").next_to(br, UR*0.2)
        # anim_1
        grp_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
        grp_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
        grp_d1 = VGroup(dot_d1,mrk_d1)
        grp_f1 = VGroup(dot_f1, mrk_f1)
        grp_ang = VGroup(a,a_value)
        grp_q = VGroup(br, distance_q)

        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
        fig_1.generate_target()
        fig_1.target.move_to((0,2,0)).scale(0.7)

        txt_2 = self.my_text(self.txt.txt['2']).shift(UP*2)
        txt_3a = self.my_text(self.txt.txt['3a']).shift(DOWN)
        txt_3b = self.my_text(self.txt.txt['3b']).next_to(txt_3a,DOWN*3)
        fml_1a = self.my_tex(self.txt.fml['1a']).next_to(txt_3a,DOWN)
        fml_2a = self.my_tex(self.txt.fml['2a']).next_to(txt_3b,DOWN)

        self.play(Write(grp_txt_1), run_time=4)
        self.play(Create(ax))
        self.play(Write(grp_f), Write(grp_d))
        self.wait(0.5)
        self.play(Write(curv1))
        self.play(Write(grp_d1), Write(grp_f1))
        self.play(Write(dsd_line))

        self.play(Unwrite(grp_txt_1),run_time=0.8)
        self.wait()
        self.play(Write(txt_2))
        
        self.play(FadeIn(grp_q))
        self.play(Write(grp_ang))
        self.play(Unwrite(txt_2),run_time=0.8)
        self.play(MoveToTarget(fig_1))
        
        self.play(Write(txt_3a),Write(fml_1a))
        self.wait()
        self.play(Write(txt_3b),Write(fml_2a))
        self.wait()



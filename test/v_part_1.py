from manim import *
from source_text import TxtLib

class V_P1(Scene):
    txt = TxtLib()
    def mytext(self, content):
        return MarkupText(content, font_size=26)
    
    def mytex(self, content, ft_size=36):
        return Tex(content, font_size=ft_size)


    def construct(self):
        # v_part_1:
        # show question
        question =  self.mytext(self.txt.txt['1_1'] + "\n" + 
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

        mrk_d = self.mytext("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = self.mytext("D<sub>1</sub>").next_to(dot_d1, UP*0.6)
        mrk_f = self.mytext("F").next_to(dot_fox, UL*0.6)
        mrk_f1= self.mytext("F<sub>1</sub>").next_to(dot_f1, DOWN*0.6)

        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = self.mytext("v<sub>1</sub>").next_to(arrow_f, DOWN)
        mrk_v2 = self.mytext("v<sub>2</sub>").next_to(arrow_d, LEFT)
        # show the simulated curve
        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
        # add parameters
        dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = Tex(r"$\theta$", font_size=26).next_to(a, LEFT*0.6)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        distance_q = self.mytext("q").next_to(br, UR*0.2)
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

        txt_2 = self.mytext(self.txt.txt['2']).shift(UP*2)
        txt_3a = self.mytext(self.txt.txt['3a']).shift(DOWN)
        txt_3b = self.mytext(self.txt.txt['3b']).next_to(txt_3a,DOWN*3)
        fml_1a = self.mytex(self.txt.fml['1a']).next_to(txt_3a,DOWN)
        fml_2a = self.mytex(self.txt.fml['2a']).next_to(txt_3b,DOWN)
        fml_1a.generate_target()
        fml_1a.target.move_to((3,0.5,0))
        fml_2a.generate_target()
        fml_2a.target.next_to(fml_1a.target,DOWN).align_to(fml_1a.target.get_left(), LEFT)
        def myarrow(start=(0,0,0), end=(1,0,0)):
            return Arrow(start,end,color=BLUE).set_opacity(0.7)

        arr1 = myarrow((1.5,0,0), (0.5,-1,0))
        grp_fml3 = VGroup(self.mytex(self.txt.fml['3a']), 
                           self.mytex(self.txt.fml['4a'])
                           ).arrange(DOWN).move_to((0,-2,0))
        txt_4 = self.mytext(self.txt.txt['4']).move_to((-3,3,0))
        txt_5 = self.mytext(self.txt.txt['5']).next_to(txt_4.get_center(), DOWN*2)

        arr2 = myarrow((1,0,0),(-1,0,0))
        txt_6 = self.mytext(self.txt.txt['6']).move_to((0,3,0))
        grp_fml5a6a = VGroup(self.mytex(self.txt.fml['5a']), 
                          self.mytex(self.txt.fml['6a'])
                          ).arrange(DOWN).move_to((-3.5,0.2,0))

        grp_fml5b6b = VGroup(self.mytex(self.txt.fml['5b']), 
                          self.mytex(self.txt.fml['6b'])
                          ).arrange(DOWN).move_to((-3.5,0.2,0))
        grp_fmlto6c_1 = VGroup(self.mytex(self.txt.fml['5b6bto6c-left1'], ft_size=40)).move_to((-3.5,0.2,0))
        
        self.play(Write(grp_txt_1), run_time=4)
        self.play(Create(ax))
        self.play(Write(grp_f), Write(grp_d))
        self.wait(0.5)
        self.play(Write(curv1))
        self.play(Write(grp_d1), Write(grp_f1))
        self.play(Write(dsd_line))
        # v_part_2
        self.play(Unwrite(grp_txt_1),run_time=0.8)
        self.wait()
        self.play(Write(txt_2))
        #
        self.play(FadeIn(grp_q))
        self.play(Write(grp_ang))
        self.play(Unwrite(txt_2),run_time=0.8)
        self.play(MoveToTarget(fig_1))
        
        self.play(Write(txt_3a),Write(fml_1a))
        self.wait()
        self.play(Write(txt_3b),Write(fml_2a))
        self.wait()
        #self.play(FadeOut(fig_1))

        self.play(FadeOut(txt_3a),FadeOut(txt_3b))
        
        self.play(MoveToTarget(fml_1a),MoveToTarget(fml_2a))
        self.wait()
        self.play(Write(txt_4),Write(arr1))
        self.play(Write(grp_fml3))
        self.play(FadeOut(arr1))
        self.play(Write(txt_5), FadeIn(arr2))
        self.play(Write(grp_fml5a6a))
        self.play(FadeOut(arr2))
        self.play(FadeOut(grp_fml3),FadeOut(fml_1a),FadeOut(fml_2a))
        self.play(Transform(grp_fml5a6a, grp_fml5b6b))
        self.wait()
        self.play(FadeOut(txt_4),Transform(txt_5, txt_6))
        self.wait()
        self.play(ReplacementTransform(grp_fml5b6b, grp_fmlto6c_1))


             




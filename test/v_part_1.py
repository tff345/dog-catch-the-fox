from manim import *
from source_text import TxtLib

class V_P1(Scene):
    
    def mytex(self, content, ft_size=36):
            return MathTex(content, font_size=ft_size)


    def construct(self):
        # v_part_1:
        txt = {
            "title" : "猎犬追狐问题",
            "1_1" : '一狐F以恒速<i>v<sub>1</sub></i>沿x轴逃跑，一犬以恒速v<sub>2</sub>追击，速度方向始终对准狐。', 
            '1_2' : "t=0 时刻, 狐在x轴上的F处，犬在D处，且DF⊥x轴，DF=L，设v<sub>2</sub>>v<sub>1</sub>，求犬的轨迹方程。", 
            '2' : r'设D<sub>1</sub>与F<sub>1</sub>间距离为<i>q</i>，FF<sub>1</sub>与DF夹角为θ，', 
            '3a' : 'FF<sub>1</sub>方向上的位置关系为 ' , 
            '3b' : "DF<sub>1</sub>方向上的位置关系为 ", 
            '4' : "两式关于时间t求导得到速度关系式",
            '5' : "同时我们有位置关系的积分表示", 
            '6' : r"消去积分项，我们可以得到$t$与$\theta$，$q$的关系", 
            
        }
        fml = {
            '1a' : r" x_{1} &= x_{2} + q\cdot \cos x ", 
            '2a' : r" x_{1}' &= x_{2}' + q ", 
            '3a' : r" v_{1} &= v_{2}\cdot\cos \theta +\frac{\mathrm{d} (q\cdot \cos q)}{\mathrm{d} t} ",
            '4a' : r" v_{1}\cdot\cos \theta &= v_{2} + \frac{\mathrm{d} q}{\mathrm{d} t} ", 
            '5a' : r" v_{1} t_{1} &= \int_{0}^{t_{1}}(v_{2} \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta ",
            '6a' : r" \int_{0}^{t_{1}}(v_{1} \cdot \cos \theta )+L &= v_{2} t_{1} + q ", 
            '5bl' : r" v_{2} \int_{0}^{t_{1}} \cos \theta \mathrm{d}t",
            '5br' : r" &= v_{1} t_{1} - q \cdot \cos \theta ",
            '6bl' : r' v_{1} \int_{0}^{t_{1}} \cos \theta \mathrm{d}t',
            '6br' : r'&= v_{2} t_{1} + q - L ', 
            '6c-l1' : r"\frac{v_{2}}{v_{1}} ",
            '6c-r1' : r'=\frac{v_{1} t_{1} - q \cdot \cos \theta}{v_{2} t_{1} + q - L} ',
            '6c-2' : r'', 
            '8' : r"(\frac{1}{m} \csc \theta - \cot \theta )\mathrm{d} \theta =\frac{\mathrm{d} q}{q} ", 
            'finalfml' : r"""
            x=-\frac{L}{2\left(1-m\right)}\left(\frac{y}{L}\right)^{\left(1-m\right)}+\frac{L}{2\left(1+m\right)}\left(\frac{y}{L}\right)^{\left(1+m\right)}+\frac{mL}{1-m^{2}}
            """
        }
        def mytext(content):
            return MarkupText(content, font_size=26)
        
        # show question
        question =  MarkupText(
             r"一狐F以恒速<i>v<sub>1</sub></i>沿<i>x</i>轴逃跑，一犬以恒速<i>v<sub>2</sub></i>追击，速度方向始终对准狐。<i>t=0 </i>时刻，"
             "\n""\n"
             r"狐在<i>x</i>轴上的F处，犬在D处，且DF⊥<i>x</i>轴，DF=L，设<i>v<sub>2</sub>>v<sub>1</sub></i>，求犬的轨迹方程。",
             justify=True
             )
        
        question.set_color(YELLOW).scale(0.5).shift(UP*3)
        self.play(Write(question), run_time=3)
        # draw the figure
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

        mrk_d = mytext("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = mytext("D<sub>1</sub>").next_to(dot_d1, UP*0.6)
        mrk_f = mytext("F").next_to(dot_fox, UL*0.6)
        mrk_f1= mytext("F<sub>1</sub>").next_to(dot_f1, DOWN*0.6)

        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = mytext("<i>v<sub>1</sub></i>").next_to(arrow_f, DOWN)
        mrk_v2 = mytext("<i>v<sub>2</sub></i>").next_to(arrow_d, LEFT)
        # show the simulated curve
        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
        # add parameters
        dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        # anim_1
        grp_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
        grp_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
        grp_d1 = VGroup(dot_d1,mrk_d1)
        grp_f1 = VGroup(dot_f1, mrk_f1)

        self.play(Write(grp_f), Write(grp_d))
        self.wait(0.5)
        self.play(Write(curv1))
        self.play(Write(grp_d1), Write(grp_f1))
        self.play(Write(dsd_line))
        self.wait(2)

        txt_2 = mytext(
             r'设D<sub>1</sub>与F<sub>1</sub>间距离为<i>q</i>，FF<sub>1</sub>与DF夹角为θ，'
             ).shift(UP*1.7)
        self.play(Write(txt_2))
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = MathTex(r"\theta", font_size=26).next_to(a, LEFT*0.6)
        grp_ang = VGroup(a,a_value)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        br_txt = br.get_tex('q')
        grp_q = VGroup(br, br_txt)
        self.play(FadeIn(grp_q))
        self.play(Write(grp_ang))
        
        self.play(Unwrite(txt_2),run_time=0.8)
        self.play(Unwrite(question),run_time=0.8)

        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
        self.play(fig_1.animate.scale(0.7).shift(UP*4))
        self.wait()
        
        txt_3a = mytext('FF<sub>1</sub>方向上的位置关系为 ').shift(DOWN)
        txt_3b = mytext("DF<sub>1</sub>方向上的位置关系为 ").next_to(txt_3a,DOWN*3)
        fml_1a = self.mytex(r" x_{1} = x_{2} + q\cdot \cos x ").next_to(txt_3a,DOWN)
        fml_2a = self.mytex(r" x_{1}' = x_{2}' + q ").next_to(txt_3b,DOWN)
        
        self.play(Write(txt_3a),Write(fml_1a))
        self.wait()
        self.play(Write(txt_3b),Write(fml_2a))
        self.wait()
        
        self.play(FadeOut(txt_3a),FadeOut(txt_3b))
        self.wait()
        fml_1_displacement_relation = MathTex(
             r" x_{1} &= x_{2} + q\cdot \cos x ",
             r"\\",          
             r" x_{1}' &= x_{2}' + q ",font_size=40
             ).move_to((3,0.5,0))
        self.play(ReplacementTransform(VGroup(fml_1a,fml_2a),fml_1_displacement_relation))
        self.play(FadeOut(fig_1,direction=UP))
        self.wait()

        arr1 = MathTex("\Longleftarrow", font_size=36).rotate(PI/4).move_to((1,-0.5,0))
        txt_4 = mytext('两式关于时间<i>t</i>求导得到速度关系式').move_to((-3,2.5,0))        
        self.play(Write(txt_4),FadeIn(arr1))

        fml3_velocity_relation = MathTex(
             r'&v_{1} = v_{2}\cdot\cos \theta +\frac{\mathrm{d} (q\cdot \cos q)}{\mathrm{d} t}'
             r'\\'
             r'&v_{1}\cdot\cos \theta = v_{2} + \frac{\mathrm{d} q}{\mathrm{d} t}',
             font_size=36).move_to((0,-2,0))
        self.play(Write(fml3_velocity_relation))
        self.play(FadeOut(arr1))
        
        txt_5 = mytext('同时我们有位置关系的积分表示').next_to(txt_4.get_center(), DOWN*2)
        arr2 = MathTex("\Longleftarrow", font_size=36).move_to((0,0.5,0))
        fml5a6a = MathTex(
          r" & v_{1} t_{1} = \int_{0}^{t_{1}}(v_{2} \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta \\ ",
          r" & \int_{0}^{t_{1}}(v_{1} \cdot \cos \theta )\mathrm{d}t+L = v_{2} t_{1} + q ",
          font_size=36).move_to((-3.5,0.4,0))
        self.play(Write(txt_5), FadeIn(arr2))
        self.play(Write(fml5a6a))
        
        txt_6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))
        self.play(FadeOut(arr2))
        self.play(
             FadeOut(fml3_velocity_relation, direction=RIGHT),
             FadeOut(fml_1_displacement_relation, direction=RIGHT)
             )
        
        grp_fml5b6b = MathTex(
          r" v_{2} \cdot \int_{0}^{t_{1}} \cos \theta \mathrm{d}t",
          r" &= v_{1} t_{1} - q \cdot \cos \theta \\ ",
          r" v_{1} \cdot \int_{0}^{t_{1}} \cos \theta \mathrm{d}t",
          r"&= v_{2} t_{1} + q - L ",
          font_size=36 
          ).move_to((-3.5,0.5,0))
        self.play(
             TransformMatchingShapes(fml5a6a[0], grp_fml5b6b[:2]),
             TransformMatchingShapes(fml5a6a[1], grp_fml5b6b[2:])
             )
        self.wait()
        self.play(FadeOut(txt_4),Transform(txt_5, txt_6))
        self.wait()
        
        fmlto6c_1 = MathTex(
            r" { {{ v_2 }} \over  {{ v_1 }}  }",
            r"= { {{v_1 t_1 - q \cdot \cos \theta}} \over {{ v_2 t_1 + q - L }} }",
            font_size=40
        ).move_to((-2.5,0.5,0))
        #self.add(fmlto6c_1)
        self.play(
             TransformMatchingShapes(VGroup(grp_fml5b6b[0],grp_fml5b6b[2]), fmlto6c_1[0]),
             TransformMatchingShapes(VGroup(grp_fml5b6b[1],grp_fml5b6b[3]), fmlto6c_1[1])
             )
        self.wait()
        fmlto6c_2 = MathTex(
             r"{{ v_2 }} ( {{ v_2 t_1 + q - L}})",
             r"={{ v_1 }} ( {{v_1 t_1 - q \cdot \cos \theta}} )",
             font_size=40
        ).move_to((-2.5,0.5,0))
        self.play(
             TransformMatchingTex(fmlto6c_1,fmlto6c_2)
        )    

from manim import *


# f_part_1:
class V_P1(Scene):     
    def construct(self):
        self.camera.background_color = "#333233"
        def mytext(content):
           return MarkupText(content, font_size=26)
        
        def mytex(content):
            return MathTex(content,font_size=36)
    
       # show question

        question = VGroup(
            mytext("一狐"),mytex("F"),mytext("以恒速"),mytex("v_1"),
            mytext("沿"),mytex("x"),mytext("轴逃跑，一犬以恒速"),mytex("v_2"),
            mytext("追击，速度方向始终对准狐."),
            mytex("t=0"),
            mytext("时刻，"),
            mytext("狐在"),mytex("x"),mytext("轴上的"),mytex("F"),mytext("处，犬在"),
            mytex("D"),mytext("处，且"),mytex(r"DF\bot x"),mytext("轴，"),
            mytex("DF = L."),mytext("设"),mytex("v_2 > v_1"),
            mytext("，求犬的轨迹方程.")
        )
        qstn1 = question[:9].arrange(RIGHT).move_to((0,3,0))
        qstn2 = question[9:21].arrange(RIGHT).move_to(qstn1.get_bottom()+DOWN*0.3).align_to(qstn1,LEFT)
        qstn3 = question[21:].arrange(RIGHT).move_to(qstn2.get_bottom()+DOWN*0.3).align_to(qstn2,LEFT)
        question = VGroup(qstn1, qstn2, qstn3)
        question.set_color(YELLOW)
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
        mrk_d = mytex("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = mytex("D_1").next_to(dot_d1, UP*0.6)
        mrk_f = mytex("F").next_to(dot_fox, UL*0.6)
        mrk_f1= mytex("F_1").next_to(dot_f1, DOWN*0.6)
 
        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = mytex("v_1").next_to(arrow_f, DOWN)
        mrk_v2 = mytex("v_2").next_to(arrow_d, LEFT)
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
        txt2 = mytext(
            r'设D<sub>1</sub>与F<sub>1</sub>间距离为<i>q</i>，FF<sub>1</sub>与DF夹角为<i>θ</i>，'
            ).shift(UP*1.7)
        txt2 = VGroup(
            mytext("设"),mytex("D_1"),mytext("与"),mytext("F_1"),
            mytext("间距离为"),mytex(r"q,\:FF_1"),mytext("与"),mytex("DF"),
            mytext("夹角为"), mytex(r"\theta")
        ).arrange(RIGHT).next_to(question.get_bottom(),DOWN)
        self.play(Write(txt2))
        a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
        a_value = MathTex(r"\theta", font_size=26).next_to(a, LEFT*0.6)
        grp_ang = VGroup(a,a_value)
        br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
        br_txt = br.get_tex('q')
        grp_q = VGroup(br, br_txt)
        self.play(FadeIn(grp_q))
        self.play(Write(grp_ang))
       
        self.play(Unwrite(txt2),run_time=0.8)
        self.play(Unwrite(question),run_time=0.8)
        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
        self.play(fig_1.animate.scale(0.6).shift(UP*4+RIGHT*5))
        self.wait()
        # # # 
        
        self.next_section("section_0")
        txt3a = mytext('FF<sub>1</sub>方向上的位置关系为 ')
        txt3b = mytext("DF<sub>1</sub>方向上的位置关系为 ").next_to(txt3a,DOWN*3)
        fml_1a = mytex(r" x_1 = x_2 + q\cdot \cos x ").next_to(txt3a,DOWN)
        fml_2a = mytex(r" x_1' = x_2' + q ").next_to(txt3b,DOWN)
       
        self.play(Write(txt3a),Write(fml_1a))
        self.wait()
        self.play(Write(txt3b),Write(fml_2a))
        self.wait()
       
        self.play(FadeOut(txt3a),FadeOut(txt3b))
        self.wait()
        fml_1_displacement_relation = MathTex(
            r" x_1 &= x_2 + q\cdot \cos x ",
            r"\\",          
            r" x_1' &= x_2' + q ",font_size=40
            ).move_to((3,0.5,0))
        self.play(ReplacementTransform(VGroup(fml_1a,fml_2a),fml_1_displacement_relation))
        self.wait()
        arr1 = MathTex("\Longleftarrow", font_size=36).rotate(PI/4).move_to((1,-0.5,0))
        txt4 = mytext('两式关于时间<i>t</i>求导得到速度关系式').move_to((-3,2.5,0))        
        self.play(Write(txt4),FadeIn(arr1))
        fml3_velocity_relation = MathTex(
            r'&v_1 = v_2\cdot\cos \theta +\frac{\mathrm{d} (q\cdot \cos q)}{\mathrm{d} t}'
            r'\\',
            r'&v_1\cdot\cos \theta = v_2 + \frac{\mathrm{d} q}{\mathrm{d} t}',
            font_size=36
        ).move_to((0,-2,0))
        self.play(Write(fml3_velocity_relation))
        self.play(FadeOut(arr1))
        """
        txt5 = mytext('同时我们有位置关系的积分表示').next_to(txt4,DOWN).align_to(txt4, LEFT)
        arr2 = MathTex("\Longleftarrow", font_size=36).move_to((0,0.5,0))
        fml5a6a = MathTex(
        r" & v_1 t_1 = \int_{0}^{t_1}(v_2 \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta \\ ",
        r" & \int_{0}^{t_1}(v_1 \cdot \cos \theta )\mathrm{d}t+L = v_2 t_1 + q ",
        font_size=36
        ).move_to((-3.5,0.4,0))
        self.play(Write(txt5), FadeIn(arr2))
        self.play(Write(fml5a6a))
        self.play(FadeOut(fig_1,shift=UR))
        
        txt6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))
        self.play(FadeOut(arr2))
        self.play(
            FadeOut(fml3_velocity_relation, scale=0.4),
             FadeOut(fml_1_displacement_relation, scale=0.4)
             )
        
        fml5b6b = MathTex(
              r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
              r" &= v_1 t_1 - q \cdot \cos \theta \\ ",
              r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
               r"&= v_2 t_1 + q - L ",
               font_size=36 
               ).move_to((-3.5,0.5,0))
        self.play(
            TransformMatchingShapes(fml5a6a[0], fml5b6b[:2]),
            TransformMatchingShapes(fml5a6a[1], fml5b6b[2:])
            )
        self.wait()
        self.play(FadeTransform(VGroup(txt4,txt5),txt6))
        self.wait()
       
        fmlto6c_1 = MathTex(
           r" \frac { v_2 } { v_1 }",
           r"= \frac { v_1 t_1 - q \cdot \cos \theta } { v_2 t_1 + q - L }",
           font_size=40
        ).move_to(fml5b6b.get_center())
        
        self.play(
           TransformMatchingShapes(VGroup(fml5b6b[0],fml5b6b[2]), fmlto6c_1[0]),
           TransformMatchingShapes(VGroup(fml5b6b[1],fml5b6b[3]), fmlto6c_1[1])
           )
        self.wait()
        fmlto6c_2 = MathTex(
            r" v_2 ( v_2 t_1 + q - L)",r"=",
            r" v_1 ( v_1 t_1 - q \cdot \cos \theta )",
            font_size=40
        ).move_to((-2.5,0.5,0))
        self.play(
            TransformMatchingShapes(fmlto6c_1,fmlto6c_2)
       )    
        fmlto6c_3 = MathTex(
              r"v_2^2 t_1 + v_2 q-v_2L ","=",
              r" v_1^2t_1-v_1 q\cos \theta",
              font_size=40
              ).move_to(fmlto6c_2.get_center())
        self.play(
           *[ReplacementTransform(fmlto6c_2[i], fmlto6c_3[i]) for i in range(0,3)]
           )
        fmlto6c_4 = MathTex(
              r"(v_2^2-v_1^2)t_1 = -(v_1\cos\theta+v_2)q+v_2L",
              substrings_to_isolate=[r"v_2^2-v_1^2"],
              font_size=40
              ).move_to(fmlto6c_3.get_center())
        self.play(
           ReplacementTransform(fmlto6c_3,fmlto6c_4)
           )
        fml6c = MathTex(
            r"t_1=",r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=40
         ).move_to(fmlto6c_4.get_bottom())
        self.play(TransformMatchingShapes(fmlto6c_4,fml6c))
       
        txt6 = mytext(
            r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系"
            ).move_to((-2.5,2,0))      
        txt7 = mytext(
             "由此，D的横坐标<i>x<sub>2</sub></i>，或<i>x</i>，可以用<i>q</i>，<i>θ</i>表示"
           ).next_to(txt6,DOWN)
        self.play(FadeTransform(txt6,txt7))
        fmlto7 = MathTex(
           r"{{x_1}}","=","{{x_2}}","+ ",r"{{q\cdot \cos x}} ",
           font_size=36
        ).next_to(fml6c, RIGHT*2)
        self.play(
            SpinInFromNothing(fmlto7)
        )
        self.play(    
            Indicate(fmlto7)
           )
        fmlto7_1 = MathTex(
            "{{x_2}}","=","-",r"{{q\cdot \cos x}} ","+","{{x_1}}",
            font_size=36
            ).move_to(fmlto7)
        fmlto7_2 = MathTex(
            "{{x}}","=","-",r"{{q\cdot \cos x}} ","+","{{v_1 t_1}}",
           font_size=36
           ).move_to(fmlto7)
        self.play(
            TransformMatchingTex(fmlto7,fmlto7_1,transform_mismatches=True)
        )
        self.play(
            TransformMatchingTex(fmlto7_1,fmlto7_2,key_map={"x_1":"v_1 t_1"})
            )
        self.play(
           fmlto7_2.animate.move_to((-4,0,0)),
           fml6c.animate.move_to(fmlto7.get_center())
        )
        fmlto7_3 = MathTex(
           "{{x}}","=","-",r"{{q\cdot \cos x}} ","+","v_1",
           r"(-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q+ \frac{v_2}{ v_2^2-v_1^2 } \cdot L)",
           font_size=36
        ).align_to(fmlto7_2,LEFT)
       
        self.play(
            FadeOut(fml6c),
            ReplacementTransform(fmlto7_2[-1],fmlto7_3[-2])
        )
        fmlto7_4 = MathTex(
           "{{x}}","=","-",r"{{q\cdot \cos x}} ",
           r"-(",r"\frac{v_1^2 \cos \theta +v_1 v_2}{v_2^2-v_1^2}",
           r" \cdot q+ ",r"\frac{v_1v_2}{ v_2^2-v_1^2 } \cdot L)",
           font_size=36
           ).align_to(fmlto7_2,LEFT)
        self.play(
           TransformMatchingShapes(fmlto7_2[-3:],fmlto7_4[4:])
        )
        self.clear()
        self.add(fmlto7_4)
        txt8 =VGroup(
            Text('这里记',font_size=26),
            MathTex(r'm=\frac{v_1}{v_2}, m \in (0,1), ',font_size=36),
            Text('于是有',font_size=26)
        ).arrange(RIGHT).move_to(txt6.get_center())
        self.play(
           FadeTransform(VGroup(txt6,txt7),txt8)
       )
        fmlto7_5 = MathTex(
            "{{x}}","=","-",r"{{q\cdot \cos x}} ",
            r"-(",r"\frac{m^2 \cos \theta +m}{1-m^2}",
            r" \cdot q+ ",r"\frac{m}{1-m^2} \cdot L)",
            font_size=36
        ).align_to(fmlto7_4,LEFT)
        self.add(txt8)
        self.play(
           ReplacementTransform(fmlto7_4,fmlto7_5)
        )
        self.wait() 
        # # # 
        self.next_section("section_1")

        fmlto7_6 = MathTex(
            "x =",r"- (\cos x+ ",r"\frac{m^2 \cos \theta +m}{1-m^2})",
            r"\cdot q -",r" \frac{m}{1-m^2} \cdot L",
            font_size=36
        ).align_to(fmlto7_5,LEFT)
        fml7 = MathTex(
            "x = ","-",r" \frac{q\cdot\cos\theta + mq}{1-m^2} ",
            "+",r" \frac{mL}{1-m^2}",
            font_size=36
        ).align_to(fmlto7_5,LEFT)
        self.play(TransformMatchingShapes(fmlto7_5,fmlto7_6))
        self.play(TransformMatchingShapes(fmlto7_6,fml7,transform_mismatches=True))
        self.wait(2)
        self.play(
            FadeOut(txt8,shift=UP),
            fml7.animate.scale(0.7).move_to((-4,-3,0))
        )
        
        # # # 
        txt9 = VGroup(
            mytext(r"为求出犬D的轨迹方程, 还需找出D的纵坐标"),
            mytex(r"y"),
            mytext(r"与"),
            mytex(r"q, \theta"),
            mytext(r"的关系, "),
            mytext(r"即用"),
            mytex(r"y"),
            mytext(r"来表示式中的"),
            mytex(r"q\cdot \cos \theta, q"),
        )
        txt9_1 = txt9[:5].arrange(RIGHT)
        txt9_2 = txt9[5:].arrange(RIGHT).shift(DOWN*0.6).align_to(txt9_1,LEFT)
        txt9 = VGroup(txt9_1,txt9_2).shift(UP*3)
        self.play(Write(txt9))
        """
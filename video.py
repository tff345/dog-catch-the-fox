from manim import *


# video
class V_P1(Scene):     
    def construct(self):
        self.camera.background_color = "#333233"
        def mytext(content):
           return MarkupText(content, font_size=26)
        
        def mytex(content):
            return MathTex(content,font_size=36)
    
        # show question

        self.next_section("15",skip_animations=False)

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
        curv1 = ax.plot(func,[0,0.5],stroke_width=2.5,use_vectorized=True)

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
        self.wait(3)
        txt2 = VGroup(
            mytext("设"),mytex("D_1"),mytext("与"),mytex("F_1"),
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
        self.wait()
       
        self.play(Unwrite(txt2),run_time=0.8)
        self.play(Unwrite(question),run_time=0.8)
        fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
        self.play(fig_1.animate.scale(0.6).shift(UP*4+RIGHT*5))
        # # # 
        
        self.next_section("100",skip_animations=False)
        txt3_1 = VGroup(
            mytext("设"),mytex("FF_1"),mytext("方向上的位置关系为")
        ).arrange(RIGHT)
        txt3_2 = VGroup(
            mytex("D_1F_1"),mytext("方向上的位置关系为")
        ).arrange(RIGHT).next_to(txt3_1,DOWN*3).align_to(txt3_1,LEFT)
        fml1a = mytex(r" x_1 = x_2 + q\cdot \cos \theta ").next_to(txt3_1,DOWN)
        fml2a = mytex(r" x_1' = x_2' + q ").next_to(txt3_2,DOWN)
       
        self.play(Write(txt3_1),Write(fml1a))
        self.wait()
        self.play(Write(txt3_2),Write(fml2a))
        self.wait(2)
       
        self.play(FadeOut(txt3_1),FadeOut(txt3_2))
        fml1_displacement_relation = MathTex(
            r" x_1 &= x_2 + q\cdot \cos\theta",
            r"\\",          
            r" x_1' &= x_2' + q ",font_size=40
            ).move_to((3,0.5,0))
        self.play(ReplacementTransform(VGroup(fml1a,fml2a),fml1_displacement_relation))
        self.wait()
        arr1 = MathTex("\Longleftarrow", font_size=36).rotate(PI/4).move_to((1,-0.5,0))
        txt4 = VGroup(
            mytext("两式关于时间"),mytex("t"),mytext("求导得到速度关系式")
        ).arrange(RIGHT).move_to((-3,3,0))
        self.play(Write(txt4),Write(arr1))
        fml3_velocity_relation = MathTex(
            r'&v_1 = v_2\cdot\cos \theta +\frac{\mathrm{d} \left(q\cdot \cos\theta\right)}{\mathrm{d} t}'
            r'\\',
            r'&v_1\cdot\cos \theta = v_2 + \frac{\mathrm{d} q}{\mathrm{d} t}',
            font_size=36
        ).move_to((0,-2,0))
        self.play(Write(fml3_velocity_relation))
        self.wait()
        self.play(Uncreate(arr1))
        
        txt5 = mytext('同时我们有位置关系的积分表示').next_to(txt4,DOWN).align_to(txt4, LEFT)
        arr2 = MathTex("\Longleftarrow", font_size=36).move_to((0,0.5,0))
        fml4_v_int = MathTex(
        " & v_1 t_1 ","=",r"\int_{0}^{t_1}\left(v_2 \cdot \cos \theta\right) \mathrm{d}t +q\cdot\cos\theta \\ ",
        r" & \int_{0}^{t_1}\left(v_1 \cdot \cos \theta\right)\mathrm{d}t+L","=","v_2 t_1 + q ",
        font_size=36
        ).move_to((-3.5,0.5,0))
        self.play(Write(txt5), Write(arr2))
        self.play(Write(fml4_v_int))
        
        self.wait()
        self.play(Uncreate(arr2))
        self.wait()
        self.play(
            FadeOut(fml3_velocity_relation, scale=0.4),
            FadeOut(fml1_displacement_relation, scale=0.4)
        )
        
        self.next_section("150")
        
        fml5 = MathTex(
              r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
              "&=",r"v_1 t_1 - q \cdot \cos \theta \\ ",
              r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
               "&=",r" v_2 t_1 + q - L ",
               font_size=36 
               ).move_to((-3.5,0,0))
        self.play(
            ReplacementTransform(fml4_v_int[:3], fml5[:3]),
            ReplacementTransform(fml4_v_int[3:], fml5[3:])
            )
        self.wait()
        txt6 = VGroup(
            mytext("消去积分项，我们可以得到"),mytex("t"),mytext("与"),
            mytex(r"\theta,\: q"),mytext("的关系")
        ).arrange(RIGHT).align_to(txt5,UL)
        self.play(FadeTransform(VGroup(txt4,txt5),txt6))
        self.wait()
        fmlto6 = MathTex(
            r" \frac { v_2 } { v_1 }",r"&= ", # fmlto6c_1
            r"\frac{v_1 t_1 - q\cdot\cos\theta}{v_2 t_1 + q - L}"r"\\",
            r" v_2 ( v_2 t_1 + q - L)",r"&=", # fmlto6c_2
            r" v_1 ( v_1 t_1 - q \cdot \cos \theta )"r"\\",
            r"v_2^2 t_1 + v_2 q-v_2L ",r"&=", # fmlto6c_3
            r" v_1^2t_1-v_1 q\cos \theta"r"\\", 
            r"(v_2^2-v_1^2)t_1 ",r"&=", # fmlto6c_4
            r"-(v_1\cos\theta+v_2)q+v_2L"r"\\",
            font_size=40
        ).align_to(fml5,LEFT)
        
        self.play(
        *[ReplacementTransform(
          VGroup(fml5[i],fml5[i+3]), fmlto6[i].set_y(fml5.get_y())
          ) for i in range(0,3)
         ]
        )
        self.wait()
        for n in range(0,3):
            self.play(
                ReplacementTransform(
                fmlto6[n:3*n+3],fmlto6[3*n+3:3*n+6].set_y(fml5.get_y())
                )
            )
            self.wait(0.7)
        
        fml6 = MathTex(
            r"t_1=",r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=40
         ).move_to(fmlto6[9:12].get_bottom())
        self.play(TransformMatchingShapes(fmlto6[9:12],fml6))
       
        txt7 = VGroup(
            mytext("由此，"),mytex("D"),mytext("的横坐标"),mytex("x_2"),
            mytext("即"),mytex("x"),mytext("，可以用"),mytex(r"q,\: \theta"),
            mytext("表示"),
        ).arrange(RIGHT).move_to(txt6)
        
        self.play(FadeTransform(txt6,txt7))
        fmlto7_1 = MathTex(
            "x_1","&="," ","x_2","+",r"q\cdot \cos \theta\\", # fmlto7
            "x_2","&=","-",r"q\cdot \cos \theta","+",r"x_1\\", # fmlto7_1
            "x","&=","-",r"q\cdot \cos \theta ","+",r"v_1 t_1\\", # fmlto7_2
        ).next_to(fml6, RIGHT*2)
        self.play(
            SpinInFromNothing(fmlto7_1[:6].set_y(fml6.get_y()))
        )
        self.play(Indicate(fmlto7_1[:6]))
        self.wait()
        self.play(
            TransformMatchingShapes(
            fmlto7_1[:6],fmlto7_1[6:12].set_y(fml6.get_y()),
            transform_mismatches=True)
        )
        self.play(
            ReplacementTransform(fmlto7_1[6:12],fmlto7_1[12:].set_y(fml6.get_y()))
            )
        self.play(
            fmlto7_1[12:].animate.align_to(fml6,LEFT),
            fml6.animate.align_to(fmlto7_1[6:12],RIGHT)
        )

        fmlto7_2 = MathTex(
            "x","&=",r"-q\cdot \cos\theta+v_1" # fmlto7_3
            r"\left(-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q+ \frac{v_2}{ v_2^2-v_1^2 } \cdot L\right)\\",
            "x","&=",r"-q\cdot \cos \theta" # fmlto7_4
            r"-\left(\frac{v_1^2 \cos \theta +v_1 v_2}{v_2^2-v_1^2}"
            r"\cdot q+\frac{v_1v_2}{ v_2^2-v_1^2 } \cdot L\right)\\",
            "x","&=",r"-q\cdot \cos\theta" # fmlto7_5
            r"-\left(\frac{m^2 \cos \theta +m}{1-m^2}"
            r"\cdot q+ \frac{m}{1-m^2} \cdot L\right)\\",
            "x ","&=",r"- \left( \cos\theta+\frac{m^2 \cos\theta+m}{1-m^2}\right)" # fmlto7_6
            r"\cdot q -\frac{m}{1-m^2} \cdot L\\",
            "x ","&= ",r"-\frac{q\cdot\cos\theta + mq}{1-m^2}" # fml7
            r"+\frac{mL}{1-m^2}\\",
            font_size=40
        ).align_to(fmlto7_1[12:],LEFT)
        fmlto7_y = fmlto7_1[12:].get_y()
        self.play(
            FadeOut(fml6,target_position=fmlto7_1[-1]),
            TransformMatchingShapes(fmlto7_1[12:],fmlto7_2[:3].set_y(fmlto7_y))
        )
        
        self.play(
           TransformMatchingShapes(fmlto7_2[:3],fmlto7_2[3:6].set_y(fmlto7_y))
        )
        txt8 =VGroup(
            Text('这里记',font_size=26),
            MathTex(r'm=\frac{v_1}{v_2}, m \in (0,1), ',font_size=36),
            Text('于是有',font_size=26)
        ).arrange(RIGHT).move_to(txt6.get_center())
        self.play(
           FadeTransform(VGroup(txt6,txt7),txt8)
        )
        
        self.add(txt8)
        self.play(
           ReplacementTransform(fmlto7_2[3:6],fmlto7_2[6:9].set_y(fmlto7_y))
        )
        self.wait() 
        # # # 

        self.next_section("290",skip_animations=False)

        fml7 = fmlto7_2[12:]
        self.play(TransformMatchingShapes(fmlto7_2[6:9],fmlto7_2[9:12].set_y(fmlto7_y)))
        self.play(TransformMatchingShapes(fmlto7_2[9:12],fml7.set_y(fmlto7_y)))
        self.wait(2)
        self.play(
            FadeOut(txt8,shift=UP),
            fml7.animate.scale(0.7).move_to((-4,-3,0)),
            FadeOut(fig_1,shift=UR)
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
        self.wait(2)
        txt10 = mytext(
            r"由前面的速度关系式可以得到"
        ).next_to(txt9_2,DOWN).align_to(txt9_1,LEFT)
        self.play(Write(txt10))      
        fml3_1 = MathTex(
            r"\frac{\mathrm{d}}{\mathrm{d}t}(q\cos\theta)","&=",
            r"v_1-v_2\cos\theta"
            r'\\',
            r"\frac{\mathrm{d} q}{\mathrm{d} t}","&=",
            r"v_1\cos \theta - v_2",
            font_size=36
            ).move_to(fml3_velocity_relation).shift(UP)
        self.play(SpinInFromNothing(fml3_velocity_relation.shift(UP)))
        self.wait()
        self.play(
        *[
            ReplacementTransform(
            fml3_velocity_relation[i], fml3_1[:3*i+3],
            transform_mismatches=True
            )
         for i in [0,1]
        ]
        )
        fmlto8 = MathTex(
            r"\frac{\mathrm{d}}{\mathrm{d}q}(q\cos\theta)",
            "&=",
            r"\frac{v_1-v_2\cos\theta}{v_1\cos\theta-v_2}"r"\\",
            r"\cos \theta-q\sin\theta\cdot\frac{\mathrm{d} \theta}{\mathrm{d} q}",
            "&=",
            r"\frac{m-\cos\theta}{m\cos\theta-1}"r"\\",
            r"-q\sin\theta\cdot\frac{\mathrm{d} \theta}{\mathrm{d} q}",
            "&=",
            r"\frac{m-\cos\theta}{m\cos\theta-1}-\cos \theta"r"\\",
            r"-q\sin\theta\cdot\frac{\mathrm{d} \theta}{\mathrm{d} q}",
            "&=",
            r"\frac{m\sin^2\theta}{m\cos\theta-1}"r"\\",
            r"q\frac{\mathrm{d} \theta}{\mathrm{d} q}",
            "&=",
            r"\frac{m\sin\theta}{1-m\cos\theta}"r"\\",
            r"\frac{\mathrm{d} q}{q\mathrm{d} \theta}",
            "&=",
            r"\frac{1-m\cos\theta}{m\sin\theta}"r"\\",
            r"\frac{\mathrm{d} q}{q\cdot\mathrm{d} \theta}",
            "&=",
            r"\frac{1}{m\sin\theta} -\frac{m\cos\theta}{m\sin\theta}"r"\\",
            r"\frac{\mathrm{d} q}{q\cdot\mathrm{d} \theta}",
            "&=",
            r"\frac{1}{m}\csc\theta -\cot\theta"r"\\",
            r"(\frac{1}{m}\csc\theta -\cot\theta)\cdot\mathrm{d} \theta",
            "&=",
            r"\frac{\mathrm{d} q}{q}"r"\\",
            r"\int (\frac{1}{m}\csc\theta -\cot\theta)\cdot\mathrm{d} \theta",
            "&=",
            r"\int \frac{\mathrm{d} q}{q}"r"\\",
            font_size=36
        )
        self.wait()
        txt11 = mytext(r"化简").next_to(txt9_2,DOWN).align_to(txt9_1,LEFT)
        self.play(FadeTransform(txt10,txt11))
        self.play(
        *[
            ReplacementTransform(
            VGroup(fml3_1[i],fml3_1[i+3]), fmlto8[i].set_y(0),
            transform_mismatches=True
            )
         for i in range(0,3)
         ]
        )
        for n in range(0,7):
            self.play(
            *[
            ReplacementTransform(
            fmlto8[i].set_y(0), fmlto8[i+3].set_y(0),
            transform_mismatches=True
            )
            for i in range(3*n,3*n+3)
             ]
            )
            self.wait(0.5)
        self.play(
            TransformMatchingShapes(
            fmlto8[21:24].set_y(0),fmlto8[24:27].set_y(0),
            transform_mismatches=True
            )
        )
        txt12 = mytext(
            r"此时可以对等式两侧同时积分"
        ).next_to(txt9_2,DOWN).align_to(txt9_1,LEFT)
        self.play(FadeTransform(txt11,txt12))
        fml8 = fmlto8[27:]
        self.play(
            TransformMatchingShapes(
            fmlto8[24:27].set_y(0),fml8.set_y(0),
            transform_mismatches=True
            )
        )
        self.play(fml8.animate.move_to(np.array([-1,0,0])))
        fml9 = MathTex(
            r"\frac1m\ln\lvert\tan\frac\theta2\rvert-\ln\lvert\sin\theta\rvert+C_1",
            "&=",r"\ln q +C_2"
            r"\\",
            r"\frac1m\ln(\tan\frac\theta2)-\ln(\sin\theta)",
            "&=",r"\ln q-\ln L"
            r"\\",
            r"e^{\frac1m\ln(\tan\frac\theta2)-\ln(\sin\theta)}",
            "&=",r"e^{\ln q-\ln L}"
            r"\\",
            r"\frac{(\tan\frac\theta2)^{\frac1m}}{\sin\theta}",
            "&=",r"\frac q L"
            r"\\",
            font_size=36
        ).shift(LEFT)
        self.play(
            TransformMatchingShapes(fml8, fml9[:3].move_to(fml8))
        )
        txt13 = VGroup(
            mytext(r"利用初值条件，即时间"),
            mytex(r"t=0"),
            mytext(r"时，D与F间距离"),
            mytex(r"q=L"),
            mytext(r"且"),
            mytex(r"\theta = \frac \pi 2"),
            mytext(r"可以解出"),
            mytex(r"C_1 - C_2 = \ln L")
        )
        txt13_1 = txt13[:6].arrange(RIGHT).align_to(txt9,LEFT)
        txt13_2 = txt13[6:].arrange(RIGHT).shift(DOWN*0.6).align_to(txt13_1,LEFT)
        txt13 = VGroup(txt13_1,txt13_2).move_to(txt9)
        self.play(FadeOut(*[txt12,txt9],shift=UP))
        self.play(Write(txt13))
        
        txt14 = VGroup(
            mytext(r"同时注意到"),
            mytex(r"\theta\in(0,\pi),\frac\theta2\in(0,\frac\pi2)\Rightarrow\sin\theta>0,\tan\theta>0"),
            mytext(r"所以消去绝对值与常数, 化为指数形式")
        )
        txt14_1 = txt14[:2].arrange(RIGHT).move_to(txt13.get_bottom()+DOWN*0.5)
        txt14_2 = txt14[2:].arrange(RIGHT).move_to(txt14_1.get_bottom()+DOWN*0.3).align_to(txt14_1,LEFT)
        txt14 = VGroup(txt14_1,txt14_2).align_to(txt13,LEFT)
        self.play(Write(txt14))
        self.wait(2)
        for n in range(0,3):
            self.play(
            *[
            ReplacementTransform(
            fml9[i].set_y(0), fml9[i+3].set_y(0),
            )
            for i in range(3*n,3*n+3)
             ]
            )
            self.wait(0.7)
        self.wait(2)
        txt15 = VGroup(
            mytext(r"因为"),
            mytex("y"),
            mytext(r"与"),
            mytex("q"),
            mytext(r"的关系为"),
            mytex(r"y=q\cdot\sin\theta"),
            mytext(r"，即")
        ).arrange(RIGHT).move_to(txt13).align_to(txt13,LEFT)
        txt16 = VGroup(
            mytext("所以我们想要求的"),
            mytex(r"q,q\cos\theta"),
            mytext("可以表示为")
        ).arrange(RIGHT).move_to(txt15).align_to(txt15,LEFT)

        self.play(
            FadeOut(*[txt13,txt14],shift=UP),
            fml9[-4:].animate.scale(0.8).shift(DOWN*3),
            FadeIn(fig_1)
        )
        self.play(
            Write(txt15),
        )

        self.next_section("495",skip_animations=False)
        
        fml10 = MathTex(
            "y",
            "&=",r"q\cdot\sin\theta"
            r"\\",
            "y",
            "&=",r"L\left(\tan \frac\theta2\right)^{\frac1m}"
            r"\\",
            r"\tan\frac\theta2",
            "&=",r"{\left(\frac yL\right)}^m",
            font_size=36
        )
        self.play(
            TransformFromCopy(txt15[5],fml10[:3].set_y(0))
        )
        self.play(
        *[
            ReplacementTransform(
            fml10[i].set_y(0), fml10[i+3].set_y(0),
            transform_mismatches=True
            )
         for i in range(0,3)
         ]
        )
        self.play(TransformMatchingShapes(fml10[3:6].set_y(0),fml10[6:9].set_y(0)))
        self.wait()
        self.play(
            FadeOut(fml9[-4:],shift=DOWN),
            fml10[6:9].animate.move_to(fml9[-4:]),
        )
        self.play(TransformMatchingShapes(txt15,txt16))
        fmltriangle = MathTex(
            r"\sin\theta&=\frac{2\tan\frac\theta2}{1+\tan^2\frac\theta2}"
            r"\\"
            r"\tan\theta&=\frac{2\tan\frac\theta2}{1-\tan^2\frac\theta2}",
            font_size=30,
        ).move_to((3,0,0))
        fmlto11 = MathTex(
            "q","&=",
            r"\frac y{\sin\theta}"r"\\"r"\\",
            r"q\cos\theta","&=",
            r"\frac y{\sin\theta}\cos\theta"r"\\",
            "q","&=",
            r"\frac y{\sin\theta}"r"\\"r"\\",
            r"q\cos\theta","&=",
            r"\frac y{\tan\theta}"r"\\",
            "q","&=",
            r"y\cdot\frac{1+\tan^2\frac\theta2}{2\tan\frac\theta2}"r"\\",
            r"q\cos\theta","&=",
            r"y\cdot\frac{1-\tan^2\frac\theta2}{2\tan\frac\theta2}"r"\\",
            "q","&=",
            r"\frac y2\left(\left(\frac yL\right)^{-m}+\left(\frac yL\right)^{m}\right)"r"\\",
            r"q\cos\theta","&=",
            r"\frac y2\left(\left(\frac yL\right)^{-m}-\left(\frac yL\right)^{m}\right)"r"\\",
            "q","&=",
            r"\frac L2\left(\left(\frac yL\right)^{1-m}+\left(\frac yL\right)^{1+m}\right)"r"\\",
            r"q\cos\theta","&=",
            r"\frac L2\left(\left(\frac yL\right)^{1-m}-\left(\frac yL\right)^{1+m}\right)"r"\\",
            font_size = 36
        ).move_to((-3,-1,0))
        self.play(Write(fmlto11[:6].set_y(0)))
        self.play(
            *[
            TransformMatchingShapes(
            fmlto11[i], fmlto11[i+6].set_y(fmlto11[i].get_y()),
            transform_mismatches=True
            )
         for i in range(0,6)
         ]
        )
        framebox1 = SurroundingRectangle(fmltriangle, buff =.2)
        txt17 = mytext("利用三角万能公式可以得到").move_to(txt16)
        self.play(
            Write(fmltriangle),
            FadeTransform(txt16,txt17),
            Create(framebox1)
        )
        self.play(FadeOut(framebox1))
        self.wait(2)
        for n in range(1,4):
            self.play(
                *[
                TransformMatchingShapes(
                fmlto11[i],fmlto11[i+6].set_y(fmlto11[i].get_y()),
                transform_mismatches=True
                )
                for i in range(6*n,6*n+6)
                ]
            )
            self.wait(0.7)
        self.play(
            FadeOut(fmltriangle,shift=RIGHT),
            fmlto11[-6:].animate.scale(0.8).move_to(
            fmltriangle.get_center()+(1,0,0)
            )
        )
        txt18 = mytext("带入前式，化简得到").move_to(txt17)
        self.play(
            TransformMatchingShapes(txt17,txt18),
            FadeOut(fml10[6:9],shift=DOWN),
            fml7.animate.scale(1.43).move_to((-2,0,0))
        )
        self.wait()
        fml11 = MathTex(
            "x","&=",
            r"-\frac{q\cdot\cos\theta + mq}{1-m^2}+\frac{mL}{1-m^2}"r"\\",
            "x","&=",
            r"-\frac L{2\left( 1-m\right)}\left(\frac yL\right)^{1-m}+\frac L{2\left(1+m\right)}\left(\frac yL\right)^{1+m}+\frac{mL}{1-m^2}"
            r"\\",
            font_size=36
        )
        fml11_1 = fml11[:3].move_to(fml7)
        fml12 = fml11[3:].set_y(0)
        self.play(
            Transform(fml7,fml11_1),
            FadeOut(fmlto11[-6:],shift=RIGHT)
        )
        self.play(
            FadeTransform(fml7,fml12)
        )
        txt19 = VGroup(
            mytext("式中"), mytex(r"m=\frac{v_1}{v_2},\: L"),mytext("为"),
            mytex(r"\overrightarrow{v_1},\: \overrightarrow{v_2}"),
            mytext("相垂直时点"),mytex(r"D,\: F"),mytext("间的距离")
        ).arrange(RIGHT).next_to(fml12,DOWN*1.5)
        self.play(Write(txt19))
        self.wait()
        framebox2 = SurroundingRectangle(fml12, buff =.3)
        self.play(Create(framebox2))
        self.play(FadeOut(framebox2))
        self.play(
            FadeOut(*[fig_1,txt18,txt19],shift=UP),
            fml12.animate.move_to((0,-2,0)),
        )
        self.wait()


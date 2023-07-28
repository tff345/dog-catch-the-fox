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
        question =  MarkupText(
            r"一狐F以恒速<i>v<sub>1</sub></i>沿<i>x</i>轴逃跑，一犬以恒速<i>v<sub>2</sub></i>追击，速度方向始终对准狐. <i>t=0 </i>时刻，"
            "\n""\n"
            r"狐在<i>x</i>轴上的F处，犬在D处，且DF⊥<i>x</i>轴，DF=L，设<i>v<sub>2</sub>>v<sub>1</sub></i>，求犬的轨迹方程.",
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
            r'设D<sub>1</sub>与F<sub>1</sub>间距离为<i>q</i>，FF<sub>1</sub>与DF夹角为<i>θ</i>，'
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
         
        txt_3a = mytext('FF<sub>1</sub>方向上的位置关系为 ')
        txt_3b = mytext("DF<sub>1</sub>方向上的位置关系为 ").next_to(txt_3a,DOWN*3)
        fml_1a = MathTex(r" x_{1} = x_{2} + q\cdot \cos x ",font_size=26).next_to(txt_3a,DOWN)
        fml_2a = MathTex(r" x_{1}' = x_{2}' + q ",font_size=26).next_to(txt_3b,DOWN)
       
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
            font_size=36
            ).move_to((0,-2,0))
        self.play(Write(fml3_velocity_relation))
        self.play(FadeOut(arr1))
       
        txt_5 = mytext('同时我们有位置关系的积分表示').align_to(txt_4, LEFT)
        VGroup(txt_4,txt_5).arrange(DOWN)
        arr2 = MathTex("\Longleftarrow", font_size=36).move_to((0,0.5,0))
        fml5a6a = MathTex(
        r" & v_1 t_1 = \int_{0}^{t_1}(v_2 \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta \\ ",
        r" & \int_{0}^{t_1}(v_1 \cdot \cos \theta )\mathrm{d}t+L = v_2 t_1 + q ",
        font_size=36).move_to((-3.5,0.4,0))
        self.play(Write(txt_5), FadeIn(arr2))
        self.play(Write(fml5a6a))
        
        txt_6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))
        self.play(FadeOut(arr2))
        self.play(
            FadeOut(fml3_velocity_relation, shift=RIGHT),
             FadeOut(fml_1_displacement_relation, shift=RIGHT)
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
        self.play(FadeTransform(VGroup(txt_4,txt_5),txt_6))
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
       
        txt_6 = mytext(
            r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系"
            ).move_to((-2.5,2,0))      
        txt_7 = mytext(
             "由此，D的横坐标<i>x<sub>2</sub></i>，或<i>x</i>，可以用<i>q</i>，<i>θ</i>表示"
           ).next_to(txt_6,DOWN)
        self.play(FadeTransform(txt_6,txt_7))
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
        txt_8 =VGroup(
            Text('这里记',font_size=26),
            MathTex(r'm=\frac{v_1}{v_2}, m \in (0,1), ',font_size=36),
            Text('于是有',font_size=26)
        ).arrange(RIGHT).move_to(txt_6.get_center())
        self.play(
           FadeTransform(VGroup(txt_6,txt_7),txt_8)
       )
        fmlto7_5 = MathTex(
            "{{x}}","=","-",r"{{q\cdot \cos x}} ",
            r"-(",r"\frac{m^2 \cos \theta +m}{1-m^2}",
            r" \cdot q+ ",r"\frac{m}{1-m^2} \cdot L)",
            font_size=36
        ).align_to(fmlto7_4,LEFT)
        self.add(txt_8)
        self.play(
           ReplacementTransform(fmlto7_4,fmlto7_5)
        )
        self.wait() 
        # # # 
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
            FadeOut(txt_8,shift=UP),
            FadeOut(fml7,scale=0.4)
        )
        txt_9 = VGroup(
            mytext(r"为找出犬D的轨迹方程, 还需找出D的纵坐标"),
            mytex(r"y"),
            mytext(r"与"),
            mytex(r"q, \theta"),
            mytext(r"的关系, "),
            mytext(r"即用"),
            mytex(r"y"),
            mytext(r"来表示式中的"),
            mytex(r"q\cdot \cos \theta, q"),
        )
        txt_9_1 = txt_9[:5].arrange(RIGHT)
        txt_9_2 = txt_9[5:].arrange(RIGHT).shift(DOWN*0.6).align_to(txt_9_1,LEFT)
        txt_9 = VGroup(txt_9_1,txt_9_2).shift(UP*3)
        self.play(Write(txt_9))
        txt_10 = mytext(
            r"由前面的速度关系式可以得到"
        ).next_to(txt_9_2,DOWN).align_to(txt_9_1,LEFT)
        self.play(Write(txt_10))      
        fml3_1 = MathTex(
            r'\frac{\mathrm{d}}{\mathrm{d}t}(q\cos\theta)&=v_1-v_2\cos\theta'
            r'\\',
            r'\frac{\mathrm{d} q}{\mathrm{d} t} &= v_1\cos \theta - v_2',
            font_size=36
            ).move_to(fml3_velocity_relation)
        self.play(SpinInFromNothing(fml3_velocity_relation))
        self.wait()
        self.play(
        *[
            TransformMatchingShapes(
            fml3_velocity_relation[i], fml3_1[i],
            transform_mismatches=True,path_arc=90 * DEGREES)
         for i in [0,1]
         ]
        )
        fml3_2 = MathTex(
            r"\frac{\mathrm{d}}{\mathrm{d}t}(q\cos\theta)","&=",
            r"v_1-v_2\cos\theta"r'\\',
            r"\frac{\mathrm{d} q}{\mathrm{d} t}","&=",
            r"v_1\cos \theta - v_2",
            font_size=36
            ).move_to(fml3_1)
        fml3_1.become(fml3_2)
        fmlto8_1 = MathTex(
            r"\frac{\mathrm{d}}{\mathrm{d}q}(q\cos\theta)",
            "=",
            r"\frac{v_1-v_2\cos\theta}{v_1\cos\theta-v_2}",
            font_size=36
        ).move_to(fml3_2)
        self.clear()
        self.add(fml3_2,txt_10,txt_9)
        self.play(
        *[
            ReplacementTransform(
            VGroup(fml3_2[i],fml3_2[i+3]), fmlto8_1[i],
            transform_mismatches=True
            )
         for i in range(0,3)
         ]
        )
        self.wait()
        txt9 = VGroup(
            mytext(r"为找出犬D的轨迹方程, 还需找出D的纵坐标"),
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
            r'\frac{\mathrm{d}}{\mathrm{d}t}(q\cos\theta)&=v_1-v_2\cos\theta'
            r'\\',
            r'\frac{\mathrm{d} q}{\mathrm{d} t} &= v_1\cos \theta - v_2',
            font_size=36
            ).move_to(fml3_velocity_relation).shift(UP)
        self.play(SpinInFromNothing(fml3_velocity_relation.shift(UP)))
        self.wait()
        self.play(
        *[
            TransformMatchingShapes(
            fml3_velocity_relation[i], fml3_1[i],
            transform_mismatches=True,path_arc=90 * DEGREES)
         for i in [0,1]
         ]
        )
        self.clear()
        # 能否去掉fml3_1?
        fml3_2 = MathTex(
            r"\frac{\mathrm{d}}{\mathrm{d}t}(q\cos\theta)","&=",
            r"v_1-v_2\cos\theta"
            r'\\',
            r"\frac{\mathrm{d} q}{\mathrm{d} t}","&=",
            r"v_1\cos \theta - v_2",
            font_size=36
            ).move_to(fml3_1)
        
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
        self.add(fml3_2,txt10,txt9)
        self.wait()
        txt11 = mytext(r"化简").next_to(txt9_2,DOWN).align_to(txt9_1,LEFT)
        self.play(FadeTransform(txt10,txt11))
        self.play(
        *[
            ReplacementTransform(
            VGroup(fml3_2[i],fml3_2[i+3]), fmlto8[i].set_y(0),
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
        self.play(
            TransformMatchingShapes(
            fmlto8[21:24].set_y(0),fmlto8[24:27].set_y(0),
            transform_mismatches=True
            )
        )
        txt12 = mytext(r"此时可以对等式两侧同时积分").next_to(txt9_2,DOWN).align_to(txt9_1,LEFT)
        self.play(FadeTransform(txt11,txt12))
        fml8 = fmlto8[27:]
        self.play(
            TransformMatchingShapes(
            fmlto8[24:27].set_y(0),fml8.set_y(0),
            transform_mismatches=True
            )
        )
        self.play(fml8.animate.move_to(ORIGIN))
        fml9 = MathTex(
            r"\frac{1}{m}\ln{\lvert\tan\frac{\theta}{2}\rvert}-\ln\lvert\sin\theta \rvert+C_1",
            "&=",
            r"\ln q +C_2",
            font_size=36
        )
        txt13 = VGroup(
            mytext(r"利用初值条件，即时间"),
            mytex(r"t=0"),
            mytext(r"时，D与F间距离"),
            mytex(r"q=L"),
            mytext(r"，且"),
            mytex(r"\theta = \frac \pi 2"),
            mytext(r"容易解出"),
            mytex(r"C_1 - C_2 = \ln L")
        )
        txt13_1 = txt13[:6].arrange(RIGHT).align_to(txt9,LEFT)
        txt13_2 = txt13[6:].arrange(RIGHT).shift(DOWN*0.6).align_to(txt13_1,LEFT)
        txt13 = VGroup(txt13_1,txt13_2).next_to(txt9,DOWN)
        self.play(
            Transform(txt12,txt13)
        )
        self.play(
            TransformMatchingShapes(
            fml8, fml9            
            )
        )
        self.wait()
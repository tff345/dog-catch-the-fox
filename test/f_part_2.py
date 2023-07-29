
from manim import *

class V_P2(Scene):
    def construct(self):
        self.next_section("0")
        self.camera.background_color = "#333233"
        def mytex(content):
            return MathTex(content,font_size=36)
        def mytext(content):
            return Text(content, font_size=26)
        fml3_velocity_relation = MathTex(
            r'''&v_1 = v_2\cdot\cos \theta +\frac{\mathrm{d} 
            (q\cdot \cos q)}{\mathrm{d} t}'''
            r'\\',
            r'&v_1\cdot\cos \theta = v_2 + \frac{\mathrm{d} q}{\mathrm{d} t}',
            font_size=36
            ).move_to((0,-2,0))
        fml7 = MathTex(
            "x = ","-",r" \frac{q\cdot\cos\theta + mq}{1-m^2} ",
            "+",r" \frac{mL}{1-m^2}",
            font_size=36
        )
        fml7.scale(0.7).move_to((-4,-3,0))
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
        for n in range(0,3):
            self.play(
            *[
            ReplacementTransform(
            fml9[i].set_y(0), fml9[i+3].set_y(0),
            )
            for i in range(3*n,3*n+3)
             ]
            )
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
        self.next_section("1")
        self.play(
            FadeOut(*[txt13,txt14],shift=UP),
            fml9[-4:].animate.scale(0.8).shift(DOWN*3)
        )
        self.play(
            Write(txt15),
            #FadeIn(fig_1)
        )
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
        self.play(
            FadeOut(fml9[-4:],shift=DOWN),
            fml10[6:9].animate.move_to(fml9[-4:]),
        )
        self.play(TransformMatchingShapes(txt15,txt16))
        fml_triangle = MathTex(
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
            r"\frac y{\tan\theta}"r"\\",# # #
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
        framebox = SurroundingRectangle(fml_triangle, buff =.2)
        txt17 = mytext("利用三角万能公式可以得到").move_to(txt16)
        self.play(
            Write(fml_triangle),
            FadeTransform(txt16,txt17),
            Create(framebox)
        )
        self.play(FadeOut(framebox))
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
        self.play(
            FadeOut(fml_triangle,shift=RIGHT),
            fmlto11[-6:].animate.scale(0.8).move_to(
            fml_triangle.get_center()+(1,0,0)
            )
        )
        txt18 = mytext("带入前式，化简得到").move_to(txt17)
        self.play(
            TransformMatchingShapes(txt17,txt18),
            FadeOut(fml10[6:9],shift=DOWN),
            fml7.animate.scale(1.43).move_to((-2,0,0))
        )
        fml11 = MathTex(
            "x","&=",
            r"\frac{q\cdot\cos\theta + mq}{1-m^2}+\frac{mL}{1-m^2}"r"\\",
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
        self.wait()
        
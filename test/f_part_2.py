from manim import *
class V_P2(Scene):
    def construct(self):
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
        # # #
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
        self.wait(2)
        txt_10 = mytext(
            r"由前面的速度关系式可以得到"
        ).next_to(txt_9_2,DOWN).align_to(txt_9_1,LEFT)
        self.play(Write(txt_10))      
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
        self.add(fml3_2,txt_10,txt_9)
        self.wait()
        txt_11 = mytext(r"化简").next_to(txt_9_2,DOWN).align_to(txt_9_1,LEFT)
        self.play(FadeTransform(txt_10,txt_11))
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
        txt_12 = mytext(r"此时可以对等式两侧同时积分").next_to(txt_9_2,DOWN).align_to(txt_9_1,LEFT)
        self.play(FadeTransform(txt_11,txt_12))
        fml8 = fmlto8[27:]
        self.play(
            TransformMatchingShapes(
            fmlto8[24:27].set_y(0),fml8.set_y(0),
            transform_mismatches=True
            )
        )
        self.play(fml8.animate.move_to(ORIGIN))
        self.wait()
        
from manim import *

class V_Finale(Scene):
    def construct(self):
        self.camera.background_color = "#333233"
        def mytext(content,ft_sz=26):
           return MarkupText(content, font_size=ft_sz)
        
        def mytex(content,ft_sz=36):
            return MathTex(content,font_size=ft_sz)
        
        fmlend = MathTex(
            "x","&=",
            r"-\frac L{2\left( 1-m\right)}\left(\frac yL\right)^{1-m}+"
            r"\frac L{2\left(1+m\right)}\left(\frac yL\right)^{1+m}+"
            r"\frac{mL}{1-m^2}",
            font_size=36
        ).move_to((0,-2,0))
        self.add(fmlend)
        txtf1 = mytext(
            "至此，我们已经得到了本题所求的轨迹方程。"
        ).move_to((0,2,0))
        self.play(Write(txtf1))

        txtf2 = VGroup(
            mytext("当犬追到狐时，"),mytex("y=0"),mytext("此时"),
            mytex(r"x_1=\frac{mL}{1-m^2}"),
        ).arrange(RIGHT).next_to(txtf1,DOWN)
        txtf3 = VGroup(
            mytext("由此可以求出追击用时"),
            mytex(r"t_1=\frac{x_1}{v_1}=\frac{v_2L}{v_2^2-v_1^2}")
        ).arrange(RIGHT).next_to(txtf2,DOWN)
        self.play(Write(txtf2))
        self.wait(2)
        self.play(Write(txtf3))
        self.wait(2)
        for m in [txtf1,txtf2,txtf3,]:
            self.play(
            Uncreate(m)
            )

        txtf4 = VGroup(
            mytext("作出"),mytex(r"L=0,\:m=\frac12"),mytext("时的轨迹曲线")
        ).arrange(RIGHT).next_to(txtf1,UP)
        fmlendvar = MathTex(
            r"x & = -\frac {y^{1-m}}{2\left( 1-m\right)}+"
            r"\frac {y^{1+m}}{2\left(1+m\right)}+\frac m{1-m^2}",
            font_size=36
        ).move_to(fmlend,DOWN).shift(DOWN*0.6)
        self.play(
            Write(txtf4),
            TransformMatchingShapes(fmlend,fmlendvar,transform_mismatches=True)
        )
        self.wait()
        fig_2 = SVGMobject(
            file_name="./assets/svg_image/desmos-graph(2).svg",
            height=2
            ).next_to(txtf4,DOWN*2)
        fig_3 = SVGMobject(
            file_name="./assets/svg_image/desmos-graph(1).svg",
            height=4
            ).next_to(txtf4,DOWN*0.3)
        self.play(FadeIn(fig_2))
        self.wait()
        self.play(
            FadeOut(fig_2,scale=0.4),
            FadeIn(fig_3,scale=0.4)
        )
        txtf5 = VGroup(
            mytext("*根据其物理意义，曲线",20),mytex("y > 1",25),mytext("的部分对应",20),
            mytex("t<0",25),mytext("的时刻的运动，",20),mytext("  即犬追击迎面而来的狐时的轨迹。",20)
        )
        txtf5_1 = txtf5[:-1].arrange(RIGHT)
        txtf5_2 = txtf5[-1].next_to(txtf5[:-1],DOWN).align_to(txtf5[:-1],LEFT)
        txtf5 = VGroup(txtf5_1,txtf5_2).move_to(fig_3.get_bottom())
        self.play(FadeIn(txtf5))
        self.wait(2)
        self.play(FadeOut(*[txtf5,txtf4,fig_3]))
        fig_4 = ImageMobject(
            filename_or_array="./assets/myimg2-2.png",
        ).scale(0.5)
        self.play(
            fmlendvar.animate.scale(0.7).next_to(fig_4,DOWN)
        )
        txtf6 = VGroup(
            mytext("改变"),mytex("m"),mytext("的值，画出出一系列追击曲线")
        ).arrange(RIGHT).set_opacity(0.7).next_to(fig_4,UP)
        self.play(Write(txtf6))
        self.play(FadeIn(fig_4))
        self.wait(4)
        self.play(fig_4.animate.scale(1.5))
        self.wait(2)
        self.play(FadeOut(*[fig_4,txtf6,fmlendvar],scale=3))
        txtf7 = Text("至此，关于猎犬追狐问题的讨论告一段落。",t2c={'[5:11]':'#ff9900'})
        txtf8 = Text("感谢观看",font='HarmonyOS Sans SC',color=BLUE_C)
        self.play(Write(txtf7))
        self.wait(2)
        self.play(Transform(txtf7,txtf8))
        self.wait()
        
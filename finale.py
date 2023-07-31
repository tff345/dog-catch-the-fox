from manim import *

class V_Finale(Scene):
    def construct(self):
        self.camera.background_color = "#333233"
        def mytext(content):
           return MarkupText(content, font_size=26)
        
        def mytex(content):
            return MathTex(content,font_size=36)
        
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
        ).move_to(fmlend,DL)
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
        self.play(Transform(fig_2,fig_3))
        self.wait(2)
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
            "\frac L{2\left(1+m\right)}\left(\frac yL\right)^{1+m}+"
            "\frac{mL}{1-m^2}",
            font_size=36
        ).move_to((0,-2,0))
        txtf1 = Text(
            "至此，我们已经得到了本题所求的轨迹方程。"
        )
        txtf2 = VGroup(
            mytext("当犬追到狐时，"),mytex("y=0"),mytext("此时"),
            mytex(r"x_1=\frac{mL}{1-m^2}"),
        ).arrange(RIGHT)
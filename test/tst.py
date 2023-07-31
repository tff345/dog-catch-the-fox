from manim import *


class V_Finale(Scene):
    def construct(self):
        self.camera.background_color = "#333233"
        fig_2 = SVGMobject(
            file_name="./assets/svg_image/desmos-graph(2).svg",
            height=2
            )
        fig_3 = SVGMobject(
            file_name="./assets/svg_image/desmos-graph(1).svg",
            height=5
            )
        VGroup(fig_2,fig_3).arrange(RIGHT,buff=.5)
        self.play(FadeIn(fig_2))
        self.wait()
        self.play(FadeIn(fig_3))
        self.wait()
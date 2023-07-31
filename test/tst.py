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
        fig_4 = ImageMobject(
            filename_or_array="./assets/myimg2-2.png",
            height=3
        )
        self.add(fig_4)
        
        
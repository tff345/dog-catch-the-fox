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
        ).scale(0.5)
        txtf7 = Text("至此，关于猎犬追狐问题的讨论告一段落。",t2c={'[5:11]':'#ff9900'})
        txtf8 = Text("感谢观看",font='HarmonyOS Sans SC',color=BLUE_C)
        self.play(Write(txtf7))
        self.play(Transform(txtf7,txtf8))

        #self.add(fig_4)
        
        
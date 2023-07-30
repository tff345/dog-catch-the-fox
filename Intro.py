from manim import *

class V_Intro(Scene):
    def construct(self):
        self.camera.background_color = "#333233"
        title = Title(r"猎犬追狐问题",color=GOLD,tex_template=TexTemplateLibrary.ctex)

        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait()
        introduction = MarkupText(
            "被追击者沿某一直线匀速运动，追击者从某点开始匀速追击，","这种平面追击问题称为猎犬追狐问题，",
            "在不同的情境中有时也称作“缉私艇追击走私船问题”“狐追兔问题”等。",
            "其轨迹曲线通常称为“追线”“狗追兔子线”，应当注意与“曳物线”区别开来。",
            "本视频将尝试从数学角度来分析这一运动学问题，并求解猎犬追狐的轨迹方程。"
        )


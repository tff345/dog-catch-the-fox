from manim import *

class V_Intro(Scene):
    def construct(self):
        self.camera.background_color = "#333233"
        title = Title(r"猎犬追狐问题",color=GOLD,tex_template=TexTemplateLibrary.ctex)
        def introtext(content,myfont="HarmonyOS Sans SC Light"):
            return MarkupText(
                content,font=myfont,font_size=60,justify=True
                ).scale(0.5)

        self.play(Write(title), run_time=2)
        self.wait()
        introtxt1 = introtext(
            '被追击者沿某一直线匀速运动，追击者从某点开始匀速追击，'
            '这种平面追击问题称为<span fgcolor="#ff9900">猎犬追狐问题</span>，'
            '在不同的情境中有时也称作“<span fgcolor="#f43802">缉私艇追击走私船问题</span>”'
            '“<span fgcolor="#f43802">狗追兔问题</span>”等。'
        ).shift(UP)
        introtxt2 = introtext(
            '其轨迹曲线通常称为“<span fgcolor="#fce43d">追线</span>”'
            '“<span fgcolor="#fce43d">狗追兔子线</span>”，'
            '应当注意与“<span fgcolor="#4ec8f5">曳物线</span>”区别开来。'
        ).next_to(introtxt1,DOWN)
        introtxt3 = introtext(
            '本视频将尝试从数学角度来分析这一运动学问题，并求解猎犬追狐的轨迹方程。',
            myfont="HarmonyOS Sans SC Medium"
        ).next_to(introtxt2,DOWN*1.5)

        introduction = VGroup(introtxt1,introtxt2,introtxt3)
        for m in introduction:
            self.play(Write(m,run_time=3))
            self.wait(2.5)
        self.play(FadeOut(title))
        self.play(FadeOut(introduction,shift=DOWN))
        self.wait()
        


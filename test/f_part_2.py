from manim import *


class Tst(Scene):
    def construct(self):
        grp_fml5b6b = MathTex(
          r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
          r" &= v_1 t_1 - q \cdot \cos \theta \\ ",
          r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
          r"&= v_2 t_1 + q - L ",
          font_size=36 
          ).move_to((-3.5,0.5,0))
        def mytext(content):
            return MarkupText(content, font_size=26)
        fmlto6c_1 = MathTex(
            r" \frac {  v_2  } {  v_1  }",
            r"= \frac { v_1 t_1 - q \cdot \cos \theta } {  v_2 t_1 + q - L  }",
            font_size=40
        )
        
        VGroup(fmlto6c_1[0],fmlto6c_1[1]).move_to((-2.5,0.5,0))
#        self.play(
#                 TransformMatchingShapes(VGroup(grp_fml5b6b[0],grp_fml5b6b[2]), fmlto6c_1[0]),
#                 TransformMatchingShapes(VGroup(grp_fml5b6b[1],grp_fml5b6b[3]), fmlto6c_1[1])
#             )
#        self.wait()
        fmlto6c_2 = MathTex(
             r" v_2 ( v_2 t_1 + q - L)",r"=",
             r" v_1 ( v_1 t_1 - q \cdot \cos \theta )",
             font_size=40
        ).move_to((-2.5,0.5,0))
#        self.play(
#             TransformMatchingShapes(fmlto6c_1,fmlto6c_2)
#        )    
        fmlto6c_3 = MathTex(
               r"v_2^2 t_1 + v_2 q-v_2L ","=",
               r" v_1^2t_1-v_1 q\cos \theta",
               font_size=40
               ).move_to(fmlto6c_2.get_center())
#        self.play(
#            *[ReplacementTransform(fmlto6c_2[i], fmlto6c_3[i]) for i in range(0,3)]
#            )
        fmlto6c_4 = MathTex(
               r"(v_2^2-v_1^2)t_1 = -(v_1\cos\theta+v_2)q+v_2L",
               substrings_to_isolate=[r"v_2^2-v_1^2"],
               font_size=40
               ).move_to(fmlto6c_3.get_center())
#        self.play(
#           FadeOut(fmlto6c_2),
#           ReplacementTransform(fmlto6c_3,fmlto6c_4))
        fml6c = MathTex(
            r"t_1=",r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=40
        ).move_to(fmlto6c_4.get_bottom())
        
        fmlto7 = MathTex(
            r"{{x_1}}","=","{{x_2}}","+ ",r"{{q\cdot \cos x}} ",
            font_size=36
        ).next_to(fml6c, RIGHT*2)
        self.play(
            SpinInFromNothing(fmlto7)
        )
        self.play(    
            Indicate(fmlto7)
            )
        fmlto7_1 = MathTex(
            "{{x_2}}","=","-",r"{{q\cdot \cos x}} ","+","{{x_1}}",
            font_size=36
            ).move_to(fmlto7)
        fmlto7_2 = MathTex(
            "{{x_2}}","=","-",r"{{q\cdot \cos x}} ","+","v_1 ","t_1",
            font_size=36
            ).move_to(fmlto7)

        self.play(
            TransformMatchingTex(fmlto7,fmlto7_1),
        )
        self.play(FadeTransform(fmlto7_1,fmlto7_2))
        self.play(
            fmlto7_2.animate.move_to((-4,0,0)),
            fml6c.animate.move_to(fmlto7.get_center())
        )
        fmlto7_3 = MathTex(
            "{{x_2}}","=","-",r"{{q\cdot \cos x}} ","+","v_1 ",
            r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=36
            )
        fmlto7_3[-1].next_to(fmlto7_2[-2],LEFT)
        self.play(
            ReplacementTransform()
        )
        
        
from manim import *


class Tst(Scene):
    def construct(self):
        fml5a6a = MathTex(
          r" & v_1 t_1 = \int_{0}^{t_1}(v_2 \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta \\ ",
          r" & \int_{0}^{t_1}(v_1 \cdot \cos \theta )\mathrm{d}t+L = v_2 t_1 + q ",
          font_size=36).move_to((-3.5,0.4,0))
        grp_fml5b6b = MathTex(
          r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
          r" &= v_1 t_1 - q \cdot \cos \theta \\ ",
          r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
          r"&= v_2 t_1 + q - L ",
          font_size=36 
          ).move_to((-3.5,0.5,0))
        fml_1_displacement_relation = MathTex(
             r" x_1 &= x_2 + q\cdot \cos x ",
             r"\\",          
             r" x_1' &= x_2' + q ",
             font_size=40
             ).move_to((3,0.5,0))
        # self.play(Write(grp_fml5b6b))
        # self.play(
        #     TransformMatchingShapes(fml5a6a[0], grp_fml5b6b[:2]),
        #     TransformMatchingShapes(fml5a6a[1], grp_fml5b6b[2:])
        #     )
        #self.wait()
        # self.play(FadeOut(txt_4),Transform(txt_5, txt_6))
        self.wait()
        def mytext(content):
            return MarkupText(content, font_size=26)
        fmlto6c_1 = MathTex(
            r" \frac {  v_2  } {  v_1  }",
            r"= \frac { v_1 t_1 - q \cdot \cos \theta } {  v_2 t_1 + q - L  }",
            font_size=40
        )
        #self.add(fmlto6c_1)
        VGroup(fmlto6c_1[0],fmlto6c_1[1]).move_to((-2.5,0.5,0))
        self.play(
                 TransformMatchingShapes(VGroup(grp_fml5b6b[0],grp_fml5b6b[2]), fmlto6c_1[0]),
                 TransformMatchingShapes(VGroup(grp_fml5b6b[1],grp_fml5b6b[3]), fmlto6c_1[1])
             )
        self.wait()
        fmlto6c_2 = MathTex(
             r" v_2 ( v_2 t_1 + q - L)",
             r"= v_1 ( v_1 t_1 - q \cdot \cos \theta )",
             substrings_to_isolate=["v_2","v_1",r"v_1 t_1 - q \cdot \cos \theta",r"v_2 t_1 + q - L"],
             font_size=40
        ).move_to((-2.5,0.5,0))
        self.play(
             TransformMatchingShapes(fmlto6c_1,fmlto6c_2)
        )    
        fmlto6c_3 = MathTex(
               r"v_2^2 t_1 + v_2 q-v_2L = v_1^2t_1-v_1 q\cos \theta",
               font_size=40
               ).move_to(fmlto6c_2.get_center())
        self.play(ReplacementTransform(fmlto6c_2, fmlto6c_3))
        fmlto6c_4 = MathTex(
               r"(v_2^2-v_1^2)t_1 = -(v_1\cos\theta+v_2)q+v_2L",
               substrings_to_isolate=["v_2^2-v_1^2"],
               font_size=40
               ).move_to(fmlto6c_3.get_center())
        self.play(ReplacementTransform(fmlto6c_3,fmlto6c_4))
        fml6c = MathTex(
            r"t_1",r"=-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2}+\frac{v_2}{v_2^2-v_1^2} \cdot L",
            substrings_to_isolate=["v_2^2-v_1^2"],
            font_size=40
        ).move_to(fmlto6c_4.get_bottom())
        self.play(TransformMatchingTex(fmlto6c_4,fml6c))
        
        txt_6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))      
        txt_7 = mytext(
               '由此，D的横坐标<i>x<sub>2</sub></i>，或<i>x</i>，可以用<i>q</i>，<i>θ</i>表示'
          ).next_to(txt_6,DOWN)
        self.play(FadeTransform(txt_6,txt_7))
        fmlto7 = MathTex(
            r"x_1","=","x_2",r"+ q\cdot \cos x ",
            font_size=36
        ).move_to(fml_1_displacement_relation[1].get_center())
        fmlto7[0].shift(DOWN*0.5)
        self.play(
            SpinInFromNothing(fmlto7)
        )
        self.play(    
            Indicate(fmlto7)
            )
        
        self.play(
            fmlto7
        )


        
        


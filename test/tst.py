from manim import *


class Tst(Scene):
    def construct(self):
        fml5 = MathTex(
              r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
              "&=",r"v_1 t_1 - q \cdot \cos \theta \\ ",
              r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
               "&=",r" v_2 t_1 + q - L ",
               font_size=36 
               ).move_to((-3.5,0,0))
        
        fmlto6 = MathTex(
            r" \frac { v_2 } { v_1 }",r"&= ", # fmlto6c_1
            r"\frac{v_1 t_1 - q\cdot\cos\theta}{v_2 t_1 + q - L}"r"\\",
            r" v_2 ( v_2 t_1 + q - L)",r"&=", # fmlto6c_2
            r" v_1 ( v_1 t_1 - q \cdot \cos \theta )"r"\\",
            r"v_2^2 t_1 + v_2 q-v_2L ",r"&=", # fmlto6c_3
            r" v_1^2t_1-v_1 q\cos \theta"r"\\", 
            r"(v_2^2-v_1^2)t_1 ",r"&=", # fmlto6c_4
            r"-(v_1\cos\theta+v_2)q+v_2L"r"\\",
            font_size=40
        ).align_to(fml5,LEFT)
        

        fml6 = MathTex(
            r"t_1=",r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=40
         ).move_to(fmlto6[9:12].get_bottom())
        
        fmlto7_1 = MathTex(
            "{{x_1}}","&="," ","{{x_2}}","+",r"{{q\cdot \cos \theta}}\\", # fmlto7
            "{{x_2}}","&=","-",r"{{q\cdot \cos \theta}}","+",r"{{x_1}}\\", # fmlto7_1
            "{{x}}","&=","-",r"{{q\cdot \cos \theta}} ","+",r"{{v_1 t_1}}\\", # fmlto7_2
        ).next_to(fml6, RIGHT*2)
        self.play(
            SpinInFromNothing(fmlto7_1[:6].set_y(fml6.get_y()))
        )
        self.play(Indicate(fmlto7_1[:6]))
        self.play(
            TransformMatchingShapes(
            fmlto7_1[:6],fmlto7_1[6:13].set_y(fml6.get_y()),
            transform_mismatches=True)
        )
        self.play(
            ReplacementTransform(fmlto7_1[6:13],fmlto7_1[13:].set_y(fml6.get_y()))
            )
        self.play(
            fmlto7_1[13:].animate.align_to(fml6,LEFT),
            fml6.animate.align_to(fmlto7_1[6:13],RIGHT)
           )
        fmlto7_2 = MathTex(
            "x","&=",r"-q\cdot \cos\theta+v_1" # fmlto7_3
            r"\left(-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} \cdot q+ \frac{v_2}{ v_2^2-v_1^2 } \cdot L\right)\\",
            "x","&=",r"-q\cdot \cos \theta" # fmlto7_4
            r"-\left(\frac{v_1^2 \cos \theta +v_1 v_2}{v_2^2-v_1^2}"
            r"\cdot q+\frac{v_1v_2}{ v_2^2-v_1^2 } \cdot L\right)\\",
            "x","&=",r"-q\cdot \cos\theta" # fmlto7_5
            r"-\left(\frac{m^2 \cos \theta +m}{1-m^2}"
            r"\cdot q+ \frac{m}{1-m^2} \cdot L\right)\\",
            "x ","&=",r"- \left( \cos\theta+\frac{m^2 \cos\theta+m}{1-m^2}\right)" # fmlto7_6
            r"\cdot q -\frac{m}{1-m^2} \cdot L\\",
            "x ","&= ",r"-\frac{q\cdot\cos\theta + mq}{1-m^2}" # fml7
            r"+\frac{mL}{1-m^2}\\"
        ).align_to(fmlto7_1[13:],LEFT)
    
        
        fmlto7_y = fmlto7_1[13:].get_y()
        self.play(
            FadeOut(fml6,target_position=fmlto7_1[-1]),
            TransformMatchingShapes(fmlto7_1[13:],fmlto7_2[:3].set_y(fmlto7_y))
        )
        self.play(
           TransformMatchingShapes(fmlto7_2[:3],fmlto7_2[3:6].set_y(fmlto7_y))
        )
        #self.clear()
        #self.add(fmlto7_4)
        
        self.play(
           ReplacementTransform(fmlto7_2[3:6],fmlto7_2[6:9].set_y(fmlto7_y))
        )
        self.play(TransformMatchingShapes(fmlto7_2[6:9],fmlto7_2[9:12].set_y(fmlto7_y)))
        self.play(TransformMatchingShapes(fmlto7_2[9:12],fmlto7_2[12:].set_y(fmlto7_y)))
        
       
        
        
        """ax = Axes(x_range=(-4, 4), 
                  y_range=(-3, 3),
                  x_length=9,
                  y_length=6)
        curve = ax.plot(lambda y: self.myfunc(y), color=RED)
        self.add(ax, curve)

    def myfunc(self, x):
        pm = 0.5
        pL = 2
        if x <= 0:
            x = 0
        return -(pL/2*(1-pm))*(x/pL)**(1-pm) + (pL/2*(1+pm))*(x/pL)**(1+pm) + pm*pL/(1-pm**2)
    """



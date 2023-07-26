from manim import *


class V_P1(Scene):
    
    def mytex(self, content, ft_size=36):
          return MathTex(content, font_size=ft_size)


    def construct(self):
        # v_part_1:
        
         def mytext(content):
            return MarkupText(content, font_size=26)
        
        # show question
         question =  MarkupText(
             r"一狐F以恒速<i>v<sub>1</sub></i>沿<i>x</i>轴逃跑，一犬以恒速<i>v<sub>2</sub></i>追击，速度方向始终对准狐。<i>t=0 </i>时刻，"
             "\n""\n"
             r"狐在<i>x</i>轴上的F处，犬在D处，且DF⊥<i>x</i>轴，DF=L，设<i>v<sub>2</sub>>v<sub>1</sub></i>，求犬的轨迹方程。",
             justify=True
             )
        
         question.set_color(YELLOW).scale(0.5).shift(UP*3)
         self.play(Write(question), run_time=3)
          # draw the figure
         ax = Axes(x_range=(-0.5, 3), 
                  y_range=(0, 3),
                  x_length=7,
                  y_length=3,
                  axis_config={
                      'include_ticks' : False,
                      'tip_shape': StealthTip
                      }).move_to((-1, -1, 0))
        
         self.play(Create(ax))
         dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
         dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
         dot_d1 = Dot(ax.coords_to_point(0.5, 0.446), color=GRAY_BROWN)
         dot_f1 = Dot(ax.coords_to_point(0.79, 0), color=ORANGE)

         mrk_d = mytext("D").next_to(dot_dog, UR*0.6)
         mrk_d1 = mytext("D<sub>1</sub>").next_to(dot_d1, UP*0.6)
         mrk_f = mytext("F").next_to(dot_fox, UL*0.6)
         mrk_f1= mytext("F<sub>1</sub>").next_to(dot_f1, DOWN*0.6)
  
         arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
         arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
         mrk_v1 = mytext("<i>v<sub>1</sub></i>").next_to(arrow_f, DOWN)
         mrk_v2 = mytext("<i>v<sub>2</sub></i>").next_to(arrow_d, LEFT)
         # show the simulated curve
         func = lambda x : -np.log(x+0.14)
         curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
         # add parameters
         dsd_line = DashedLine(dot_d1.get_center(),dot_f1.get_center())
         # anim_1
         grp_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
         grp_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
         grp_d1 = VGroup(dot_d1,mrk_d1)
         grp_f1 = VGroup(dot_f1, mrk_f1)
  
         self.play(Write(grp_f), Write(grp_d))
         self.wait(0.5)
         self.play(Write(curv1))
         self.play(Write(grp_d1), Write(grp_f1))
         self.play(Write(dsd_line))
         self.wait(2)

         txt_2 = mytext(
             r'设D<sub>1</sub>与F<sub>1</sub>间距离为<i>q</i>，FF<sub>1</sub>与DF夹角为<i>θ</i>，'
             ).shift(UP*1.7)
         self.play(Write(txt_2))
         a = Angle(ax.x_axis, dsd_line, radius=0.3, quadrant=(-1,-1), other_angle=True)
         a_value = MathTex(r"\theta", font_size=26).next_to(a, LEFT*0.6)
         grp_ang = VGroup(a,a_value)
         br = Brace(dsd_line, direction=dsd_line.copy().rotate(PI / 2).get_unit_vector())
         br_txt = br.get_tex('q')
         grp_q = VGroup(br, br_txt)
         self.play(FadeIn(grp_q))
         self.play(Write(grp_ang))
        
         self.play(Unwrite(txt_2),run_time=0.8)
         self.play(Unwrite(question),run_time=0.8)

         fig_1 = VGroup(ax,curv1,grp_d,grp_d1,grp_f,grp_f1,grp_ang,grp_q,dsd_line)
         self.play(fig_1.animate.scale(0.7).shift(UP*4))
         self.wait()
          
         txt_3a = mytext('FF<sub>1</sub>方向上的位置关系为 ').shift(DOWN)
         txt_3b = mytext("DF<sub>1</sub>方向上的位置关系为 ").next_to(txt_3a,DOWN*3)
         fml_1a = self.mytex(r" x_{1} = x_{2} + q\cdot \cos x ").next_to(txt_3a,DOWN)
         fml_2a = self.mytex(r" x_{1}' = x_{2}' + q ").next_to(txt_3b,DOWN)
        
         self.play(Write(txt_3a),Write(fml_1a))
         self.wait()
         self.play(Write(txt_3b),Write(fml_2a))
         self.wait()
        
         self.play(FadeOut(txt_3a),FadeOut(txt_3b))
         self.wait()
         fml_1_displacement_relation = MathTex(
             r" x_{1} &= x_{2} + q\cdot \cos x ",
             r"\\",          
             r" x_{1}' &= x_{2}' + q ",font_size=40
             ).move_to((3,0.5,0))
         self.play(ReplacementTransform(VGroup(fml_1a,fml_2a),fml_1_displacement_relation))
         self.play(FadeOut(fig_1,direction=UP))
         self.wait()

         arr1 = MathTex("\Longleftarrow", font_size=36).rotate(PI/4).move_to((1,-0.5,0))
         txt_4 = mytext('两式关于时间<i>t</i>求导得到速度关系式').move_to((-3,2.5,0))        
         self.play(Write(txt_4),FadeIn(arr1))

         fml3_velocity_relation = MathTex(
             r'&v_{1} = v_{2}\cdot\cos \theta +\frac{\mathrm{d} (q\cdot \cos q)}{\mathrm{d} t}'
             r'\\'
             r'&v_{1}\cdot\cos \theta = v_{2} + \frac{\mathrm{d} q}{\mathrm{d} t}',
             font_size=36).move_to((0,-2,0))
         self.play(Write(fml3_velocity_relation))
         self.play(FadeOut(arr1))
        
         txt_5 = mytext('同时我们有位置关系的积分表示').next_to(txt_4.get_center(), DOWN*2)
         arr2 = MathTex("\Longleftarrow", font_size=36).move_to((0,0.5,0))
         fml5a6a = MathTex(
         r" & v_1 t_1 = \int_{0}^{t_1}(v_2 \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta \\ ",
         r" & \int_{0}^{t_1}(v_1 \cdot \cos \theta )\mathrm{d}t+L = v_2 t_1 + q ",
         font_size=36).move_to((-3.5,0.4,0))
         self.play(Write(txt_5), FadeIn(arr2))
         self.play(Write(fml5a6a))
         
         txt_6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))
         self.play(FadeOut(arr2))
         self.play(
             FadeOut(fml3_velocity_relation, direction=RIGHT),
             FadeOut(fml_1_displacement_relation, direction=RIGHT)
             )
        
         fml5b6b = MathTex(
               r" v_2 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
               r" &= v_1 t_1 - q \cdot \cos \theta \\ ",
               r" v_1 \cdot \int_{0}^{t_1} \cos \theta \mathrm{d}t",
               r"&= v_2 t_1 + q - L ",
               font_size=36 
               ).move_to((-3.5,0.5,0))
         self.play(
             TransformMatchingShapes(fml5a6a[0], fml5b6b[:2]),
             TransformMatchingShapes(fml5a6a[1], fml5b6b[2:])
             )
         self.wait()
         self.play(FadeOut(txt_4),Transform(txt_5, txt_6))
         self.wait()
        
         fmlto6c_1 = MathTex(
            r" \frac { v_2 } { v_1 }",
            r"= \frac { v_1 t_1 - q \cdot \cos \theta } { v_2 t_1 + q - L }",
            font_size=40
        ).move_to(fml5b6b.get_center())
        
         self.play(
             TransformMatchingShapes(VGroup(fml5b6b[0],fml5b6b[2]), fmlto6c_1[0]),
             TransformMatchingShapes(VGroup(fml5b6b[1],fml5b6b[3]), fmlto6c_1[1])
             )
         self.wait()
         fmlto6c_2 = MathTex(
             r" v_2 ( v_2 t_1 + q - L)",r"=",
             r" v_1 ( v_1 t_1 - q \cdot \cos \theta )",
             font_size=40
        ).move_to((-2.5,0.5,0))
         self.play(
             TransformMatchingShapes(fmlto6c_1,fmlto6c_2)
        )    
         fmlto6c_3 = MathTex(
               r"v_2^2 t_1 + v_2 q-v_2L ","=",
               r" v_1^2t_1-v_1 q\cos \theta",
               font_size=40
               ).move_to(fmlto6c_2.get_center())
         self.play(
            *[ReplacementTransform(fmlto6c_2[i], fmlto6c_3[i]) for i in range(0,3)]
            )
         fmlto6c_4 = MathTex(
               r"(v_2^2-v_1^2)t_1 = -(v_1\cos\theta+v_2)q+v_2L",
               substrings_to_isolate=[r"v_2^2-v_1^2"],
               font_size=40
               ).move_to(fmlto6c_3.get_center())
         self.play(
            FadeOut(fmlto6c_2),
            ReplacementTransform(fmlto6c_3,fmlto6c_4))
         fml6c = MathTex(
            r"t_1=",r"-\frac{v_1 \cos \theta +v_2}{v_2^2-v_1^2} + \frac{v_2}{ v_2^2-v_1^2 } \cdot L",
            font_size=40
         ).move_to(fmlto6c_4.get_bottom())
         self.play(TransformMatchingShapes(fmlto6c_4,fml6c))
        
         txt_6 = mytext(r"消去积分项，我们可以得到<i>t</i>与<i>θ</i>，<i>q</i>的关系").move_to((-2.5,2,0))      
         txt_7 = mytext(
             "由此，D的横坐标<i>x<sub>2</sub></i>，或<i>x</i>，可以用<i>q</i>，<i>θ</i>表示"
           ).next_to(txt_6,DOWN)
         self.play(FadeTransform(txt_6,txt_7))
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
             "{{x_2}}","=","-",r"{{q\cdot \cos x}} ","+","{{v_1 t_1}}",
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
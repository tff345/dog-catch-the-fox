from manim import *
from source_text import TxtLib

class Tst(Scene):
    txt = TxtLib()
    def my_text(self, content):
        return MarkupText(content, font_size=20)
    
    
    def construct(self):
        ax = Axes(x_range=(-0.5, 7), 
                  y_range=(0, 5),
                  x_length=9,
                  y_length=4, 
                  axis_config={
                      'include_ticks' : False
                      }).move_to((-1, -1, 0))
        dot_dog = Dot(ax.coords_to_point(0, 2), color=GRAY_BROWN)
        dot_fox = Dot(ax.coords_to_point(0, 0), color=ORANGE)
        dot_d1 = Dot(ax.coords_to_point(0.5, 0.446), color=GRAY_BROWN)
        dot_f1 = Dot(ax.coords_to_point(0.79, 0), color=ORANGE)

        mrk_d = self.my_text("D").next_to(dot_dog, UR*0.6)
        mrk_d1 = self.my_text("D<sub>1</sub>").next_to(dot_d1, UR*0.6)
        mrk_f = self.my_text("F").next_to(dot_fox, UR*0.6)
        mrk_f1= self.my_text("F<sub>1</sub>").next_to(dot_f1, UR*0.6)

        arrow_d = Vector([0,-0.6]).next_to(dot_dog, LEFT) 
        arrow_f = Vector([0.4,0]).next_to(dot_fox, DOWN) 
        mrk_v1 = self.my_text("v<sub>1</sub>").next_to(arrow_f, DOWN)
        mrk_v2 = self.my_text("v<sub>2</sub>").next_to(arrow_d, LEFT)

        func = lambda x : -np.log(x+0.14)
        curv1 = ax.plot(func, [0,0.5], use_vectorized=True)
        dashedline = DashedLine(dot_d1.get_center(),dot_f1.get_center())
        
        group_d = VGroup(dot_dog, mrk_d, arrow_d, mrk_v2)
        group_f = VGroup(dot_fox, mrk_f, arrow_f, mrk_v1)
        group_d1 = VGroup(dot_d1,mrk_d1)
        group_f1 = VGroup(dot_f1, mrk_f1)

        self.play(Create(ax))
        self.play(Write(group_f), Write(group_d))
        self.wait()
        self.play(Write(curv1))
        self.play(Write(group_d1), Write(group_f1))
        self.play(Write(dashedline))

    
    
    
    def myfunc(self, x):
        pm = 0.5
        pL = 2
        return -(pL/2*(1-pm))*(x/pL)**(1-pm) + (pL/2*(1+pm))*(x/pL)**(1+pm) + pm*pL/(1-pm**2)

        


from manim import *


class PlotParametricFunction(Scene):
    def func(self, t):
        def myfunc(x, pm=0.5,pL=2):
            x = np.abs(x)
            return -(pL/2*(1-pm))*(x/pL)**(1-pm) + (pL/2*(1+pm))*(x/pL)**(1+pm) + pm*pL/(1-pm**2)
        
        return np.array((myfunc(t), t, 0.))

    def construct(self):
        func = ParametricFunction(
            self.func, t_range = np.array([0, 3]), fill_opacity=0, use_smoothing=False
            ).set_color(RED)
        func.scale(4).move_to((-2,2,0))
        
        fml_1_2 = MathTex(
            r" &v_{1} t_{1} = \int_{0}^{t_{1}}(v_{2} \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta ",
            r" \\ ",
            r" &\int_{0}^{t_{1}}(v_{1} \cdot \cos \theta )\mathrm{d}t+L = v_{2} t_{1} + q ",
             font_size=36).move_to((3,0.5,0))
        self.play(Create(func))
        self.wait()


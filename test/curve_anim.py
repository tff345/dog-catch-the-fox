from manim import *

def myfunc(x, pm=0.5,pL=1):
    x = np.abs(x)
    return -(pL/(2*(1-pm)))*(x/pL)**(1-pm) + (pL/(2*(1+pm)))*(x/pL)**(1+pm) + pm*pL/(1-pm**2)
class PlotParametricFunction(Scene):
    def func(self, t,pm=0.5,pL=2):
        return np.array((myfunc(t,pm,pL), t, 0.))

    def construct(self):
        func = ParametricFunction(
            self.func, t_range = np.array([0, 5]), fill_opacity=0, use_smoothing=False
            ).set_color(RED)
        func.scale(4).move_to((-2,2,0))
        ax = Axes(x_range=(0, 3), 
                  y_range=(0, 3),
                  x_length=7,
                  y_length=3,
                  axis_config={
                      'include_ticks' : False,
                      'tip_shape': StealthTip
                      })
        ax = NumberPlane()
        curv = ax.plot_parametric_curve(self.func,fill_color=BLUE)
        p1 = np.array([])
        self.add(ax)
        self.add(curv)
        self.wait()


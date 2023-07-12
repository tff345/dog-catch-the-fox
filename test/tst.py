from manim import *


class Tst(Scene):
    def construct(self):
        ax = Axes(x_range=(-4, 4), 
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
    



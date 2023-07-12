# code: UTF-8

class TxtLib():
    def __init__(self): 
        self.txt = {
            "title" : "猎犬追狐问题",
            "1_1" : '一狐F以恒速v<sub>1</sub>沿x轴逃跑, 一犬以恒速v<sub>2</sub>追击，速度方向始终对准狐。', 
            '1_2' : "t=0 时刻, 狐在x轴上的F处, 犬在D处, 且DF⊥x轴, DF=L, 设v<sub>2</sub>>v<sub>1</sub>, 求犬的轨迹方程。", 
            '2' : r'设D<sub>1</sub>与F<sub>1</sub>间距离为q, D<sub>1</sub>F<sub>1</sub>与DF夹角为θ', 
            '3' : 'FF<sub>1</sub>方向上的位置关系为 ', 
            
        }
        self.fml = {
            '1a' : r"x_{1} = x_{2} + q\cdot \cos x", 
            '2a' : r"x_{1}' = x_{2}' + q", 
            '3a' : r"v_{1} = v_{2}\cdot\cos \theta +\frac{\mathrm{d} (q\cdot \cos q)}{\mathrm{d} t}",
            '4a' : r"v_{1}\cdot\cos \theta = v_{2} + \frac{\mathrm{d} q}{\mathrm{d} t}", 
            '5a' : r"v_{1} \cdot t_{1} = \int_{0}^{t_{1}}(v_{2} \cdot \cos \theta ) \mathrm{d}t +q\cdot\cos\theta",
            '6a' : r"\int_{0}^{t_{1}}(v_{1} \cdot \cos \theta )+L=v_{2}+q", 
            '5b' : r"",
            'finalfml' : r"""
            x=-\frac{L}{2\left(1-m\right)}\left(\frac{y}{L}\right)^{\left(1-m\right)}+\frac{L}{2\left(1+m\right)}\left(\frac{y}{L}\right)^{\left(1+m\right)}+\frac{mL}{1-m^{2}}
            """

        }
        


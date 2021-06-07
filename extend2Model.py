class extend2Model:
    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1
        self.d = 1
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0

        self.x0 = 0
        self.y0 = 0

        self.end = 20

        self.imagePath = 'modelsImages/extend2Model.png'

    def __repr__(self):
        return "Drugie rozszerzenie"

    def getParametersSeters(self):
        return [("X0",lambda z:self.setX(z),0.6),
                ("Y0",lambda z:self.setY(z),0.3),
                ("A",lambda z:self.setA(z),0.1),
                ("B",lambda y:self.setB(y),0.3),
                ("C",lambda x:self.setC(x),0.2),
                ("D",lambda x:self.setD(x),0.3),
                ("G",lambda x:self.setG(x),0),
                ("H",lambda x:self.setH(x),0),
                ("Zakres:",lambda x:self.setEnd(x),100)]

    def fun_x(self,x, y):
        return (self.a - self.b * y) * x - self.e * x - self.g*x**2

    def fun_y(self,x, y):
        return (self.c * x - self.d) * y - self.f * y - self.h*y**2
    
    
    def generateData(self):
        '''
        :param x0: Preys amount
        :param y0: Predator amount
        :param step: step
        :param end: endpoint
        :param a: is the growing rate of preys, when there's no predator
        :param b: is the dying rate of preys, due to predation
        :param c: is the dying rate of predators, when there's no preys
        :param d: is the factor describing how many caught preys let create a new predator
        :param e: prey competition factor
        :param f: predator competition factor
        :param g: environment capacity factor for preys
        :param h: environment capacity factor for predators
        :return:
        '''
        step = 0.01

        t_arg = []
        x_val = []
        y_val = []

        t_curr = 0
        x_curr = self.x0
        y_curr = self.y0
        while t_curr < self.end:
            y_prev = y_curr
            y_curr = y_prev + step * self.fun_y(x_curr, y_curr)

            x_prev = x_curr
            x_curr = x_prev + step * self.fun_x(x_curr, y_curr)

            y_val.append(y_curr)
            x_val.append(x_curr)
            t_arg.append(t_curr)

            t_curr += step



        return [["Ofiary",t_arg, x_val],["Drapieżniki",t_arg, y_val]]
        
    def setX(self,A):
        self.x0 = float(A)

    def setY(self,B):
        self.y0 = float(B)
    
    
    def setA(self,A):
        self.a = float(A)

    def setB(self,B):
        self.b = float(B)

    def setC(self,A):
        self.c = float(A)

    def setD(self,A):
        self.d = float(A)

    def setG(self,A):
        self.g = float(A)

    def setH(self,A):
        self.h = float(A)

    def setEnd(self,A):
        self.end = float(A)
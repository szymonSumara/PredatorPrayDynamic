class extend3Model:
    def __init__(self):

        self.x0 = 0
        self.y0 = 0

        self.a = 0
        self.b = 0

        self.K1 = 0
        self.K2 = 0

        self.R1 = 0
        self.R2 = 0
        self.end = 20
        self.imagePath = 'modelsImages/extend3Model.png'

    def __repr__(self):
        return "Trzecie rozszerzenie "

    def getParametersSeters(self):
        return [("X0",lambda z:self.setX(z),10),
                ("Y0",lambda z:self.setY(z),10),
                ("a", lambda z:self.setA(z),0.3),
                ("b", lambda y:self.setB(y),0.2),
                ("K1",lambda x:self.setK1(x),50),
                ("K2",lambda x:self.setK2(x),20),
                ("R1",lambda x:self.setR1(x),1.1),
                ("R2",lambda x:self.setR2(x),2),
                ("End",lambda x:self.setEnd(x),20)]


    def fun_x(self,x, y):
        return self.R1*x*((self.K1-x-self.a*y)/ self.K1)

    def fun_y(self,x, y):
        return self.R2*y*((self.K2-y-self.b*x)/self.K2)
    
    def generateData(self):
        '''

        :param x0:  Preys amount
        :param y0: Predator amount
        :param h: step
        :param end: endpoint
        :param K1: environment capacity for prey
        :param K2: environment capacity for predator
        :param a: competition factor (prey)
        :param b: competition factor (predator)
        :param r1: growth of preys
        :param r2: growth of predators
        :return:
        '''

        step = 0.01
        t_arg = []
        x_val = []
        y_val = []

        t_curr = 0
        x_curr = self.x0
        y_curr = self.y0
        while t_curr < self.End:
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

    def setK1(self,A):
        self.K1 = float(A)

    def setK2(self,A):
        self.K2 = float(A)

    def setR1(self,A):
        self.R1 = float(A)

    def setR2(self,A):
        self.R2 = float(A)

    def setEnd(self,A):
        self.End = float(A)


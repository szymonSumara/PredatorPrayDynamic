class exampleModel:
    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1
        self.d = 1
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0

        self.imagePath = 'img.png'

    def __repr__(self):
        return "Nazwa modelu"

    def getParametersSeters(self):
        return [("Z",lambda z:self.setZ(z)),
                ("Y",lambda y:self.setY(y)),
                ("X",lambda x:self.setX(x))]

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

        def fun_x(x, y):
            return (a - b * y) * x - e * x - g*x**2

        def fun_y(x, y):
            return (c * x - d) * y - f * y - h*y**2

        t_arg = []
        x_val = []
        y_val = []

        t_curr = 0
        x_curr = x0
        y_curr = y0
        while t_curr < end:
            y_prev = y_curr
            y_curr = y_prev + step * fun_y(x_curr, y_curr)

            x_prev = x_curr
            x_curr = x_prev + step * fun_x(x_curr, y_curr)

            y_val.append(y_curr)
            x_val.append(x_curr)
            t_arg.append(t_curr)

            t_curr += step



        return [t_arg, x_val, y_val]

    def setZ(self,Z):
        self.Z = float(Z)
    def setY(self,Y):
        self.Y = float(Y)
    def setX(self,X):
        self.X = float(X)




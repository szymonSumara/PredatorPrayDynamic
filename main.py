import matplotlib.pyplot as mpl


def lotka_volterra1(x0, y0, h, end, a, b, c, d, e=0, f=0):
    '''
    :param x0: Preys amount
    :param y0: Predator amount
    :param h: step
    :param end: endpoint
    :param a: is the growing rate of preys, when there's no predator
    :param b: is the dying rate of preys, due to predation
    :param c: is the dying rate of predators, when there's no preys
    :param d: is the factor describing how many caught preys let create a new predator
    :param e: prey competition factor
    :param f: predator competition factor
    :return:
    '''


    def fun_x(x, y):
        return (a - b * y) * x - e * x

    def fun_y(x, y):
        return (c * x - d) * y - f * y

    t_arg = []
    x_val = []
    y_val = []

    t_curr = 0
    x_curr = x0
    y_curr = y0
    while t_curr < end:
        y_prev = y_curr
        y_curr = y_prev + h * fun_y(x_curr, y_curr)

        x_prev = x_curr
        x_curr = x_prev + h * fun_x(x_curr, y_curr)

        y_val.append(y_curr)
        x_val.append(x_curr)
        t_arg.append(t_curr)

        t_curr += h

    mpl.plot(t_arg, x_val, label="preys")
    mpl.plot(t_arg, y_val, label="predators")
    mpl.xlabel("time")
    mpl.ylabel("population")
    mpl.legend()
    mpl.show()


def lotka_volterra2(x0, y0, h, end):





if __name__ == '__main__':
    lotka_volterra1(1,0.5, 0.001, 10, 1, 1, 0.8, 0.8)

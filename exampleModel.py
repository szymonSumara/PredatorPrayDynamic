class exampleModel:
    def __init__(self):
        self.Z = 1
        self.Y = 1
        self.X = 1
        self.imagePath = 'img.png'

    def __repr__(self):
        return "Nazwa modelu"

    def getParametersSeters(self):
        return [("Z",lambda z:self.setZ(z)),("Y",lambda y:self.setY(y)),("X",lambda x:self.setX(x))]

    def generateData(self):
        return [["y1",[0,1,2],[self.Z,self.Y,self.X]],["y2",[0,1],[3,2]]]

    def setZ(self,Z):
        self.Z = float(Z)
    def setY(self,Y):
        self.Y = float(Y)
    def setX(self,X):
        self.X = float(X)




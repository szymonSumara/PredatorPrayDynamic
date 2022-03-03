import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np
from basicModel import basicModel
class ModelControls(QWidget):
    def __init__( self, model, outerClass):
        
        super().__init__()
        self.dataColectors = []
        self.outerClass = outerClass
        layout = QVBoxLayout()
        
        
        label = QLabel(self)
        pixmap = QPixmap(self.outerClass.actualSelectedModel.imagePath)
        #pixmap = pixmap.scaledToWidth(600)
        label.setPixmap(pixmap)
        label.resize( pixmap.width(), pixmap.height())
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label,0)
        layout.addStretch()
    
        for fieldLabel,setLambda,defoultValue in outerClass.actualSelectedModel.getParametersSeters():
            
            nameLabel = QLabel()
            nameLabel.setText(fieldLabel)
            newLine = QSlider(Qt.Horizontal)
            newLine.setMinimum(1)
            if defoultValue < 1:
                newLine.setMaximum(100)
                newLine.setTickInterval(5)
            elif defoultValue < 10:
                newLine.setMaximum(1000)
                newLine.setTickInterval(50)
            elif defoultValue <= 100:
                newLine.setMaximum(10000)
                newLine.setTickInterval(500)


            newLine.setValue(defoultValue*100)
            newLine.setTickPosition(QSlider.TicksBelow)
            

            row = QHBoxLayout()
            row.addWidget(nameLabel)
            row.addWidget(newLine)
            
            layout.addLayout(row)
            layout.addStretch()
            self.dataColectors.append(lambda func=setLambda,field = newLine :func(field.value()/100))
        runText = QLabel("Uruchom wizualizacje")
        layout.addWidget(runText)
        
        self.runButton1 = QPushButton('Wykresy y(t) i x(t)')
        self.runButton1.clicked.connect(lambda : self.runAction(self.outerClass.drawFunctionsYbyTandXbyT))

        self.runButton2 = QPushButton('Wykres y(x)')
        self.runButton2.clicked.connect(lambda : self.runAction(self.outerClass.drawFunctionYandX))
        self.runButton3 = QPushButton('Wykres stalej')
        self.runButton3.clicked.connect(lambda : self.runAction(self.outerClass.drawConstant))

        row = QHBoxLayout()
        row.addWidget(self.runButton1)
        row.addWidget(self.runButton2)
        
        if(isinstance(self.outerClass.actualSelectedModel, basicModel)):
            row.addWidget(self.runButton3)
            
        layout.addLayout(row)
        layout.addStretch()

        self.setLayout(layout)

    def runAction(self,function):
        for dataColector in self.dataColectors:
            dataColector()
        function(self.outerClass.actualSelectedModel.generateData())


class AppGUI(QWidget):
    def __init__(self,models):
        super().__init__()
        self.models = models
        self.title = 'Predator Pray'
        self.left = 10
        self.top = 10

        self.setFixedWidth(1600)
        self.setFixedHeight(800)
        self.actualSelectedModelControls = None
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.canvasBox  = QVBoxLayout()
        self.controlBox = QVBoxLayout()
        self.appBox = QHBoxLayout(self)
        
        self.canvasField = FigureCanvas(Figure(figsize=(5, 3)))
        self._static_ax = self.canvasField.figure.subplots()
        self.canvasBox.addWidget(self.canvasField)
        
        self.modelsList = QComboBox()
        for model in self.models:
            self.modelsList.addItem(str(model))
        self.modelsList.activated.connect(self.changeActualSelectedModel)

        self.controlBox.addWidget(self.modelsList,0)     
       
       
        self.appBox.addLayout(self.canvasBox,2)
        self.appBox.addLayout( self.controlBox,1)
        self.controlBox.addStretch()
        self.setLayout(self.appBox)       
        self.show()
        self.changeActualSelectedModel()

    def drawFunctionsYbyTandXbyT(self,newDataToShow):
        self._static_ax.cla()
        for label,x,y in newDataToShow:
            self._static_ax.plot(x, y, "-",label=label)
        self._static_ax.set_ylabel("Ilość drapierzniów i ofiar")
        self._static_ax.set_xlabel("Czas")
        self._static_ax.legend()
        self.canvasField.draw()

    def drawFunctionYandX(self,newDataToShow):
        self._static_ax.cla()
        x = newDataToShow[0][2]
        y = newDataToShow[1][2]
        self._static_ax.set_ylabel("Ilość drapierzniów")
        self._static_ax.set_xlabel("Ilość ofiar")
        self._static_ax.plot(x, y, "-")
        self.canvasField.draw()

    def drawConstant(self,newDataToShow):
        self._static_ax.cla()
        predators   = newDataToShow[1][2]
        preys       = newDataToShow[0][2]
        x           = newDataToShow[0][1]
        y = []
        for i in range(len(x)):
            y.append(-self.actualSelectedModel.d*np.log(preys[i])
                     +self.actualSelectedModel.c*preys[i]
                     -self.actualSelectedModel.a*np.log(predators[i])
                     +self.actualSelectedModel.b*predators[i])
        self._static_ax.plot(x, y, "-")
        self.canvasField.draw()


    def changeActualSelectedModel(self):
        self.actualSelectedModel = self.models[ self.modelsList.currentIndex()]
      
        if self.actualSelectedModelControls != None:
            self.controlBox.removeWidget(self.actualSelectedModelControls)
            self.actualSelectedModelControls.deleteLater()
            self.actualSelectedModelControls = None
        self.actualSelectedModelControls = ModelControls(self.actualSelectedModel, self)
       
        self.controlBox.addWidget(self.actualSelectedModelControls)
        self.controlBox.addStretch()
       
class App:
    def __init__(self,models):
        app = QApplication(sys.argv)
        ex = AppGUI(models)
        sys.exit(app.exec_())
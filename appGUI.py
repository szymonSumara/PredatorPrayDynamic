import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np

class ModelControls(QWidget):
    def __init__( self, model, updatePlotData):
        
        super().__init__()
        self.dataColectors = []
        self. updatePlotData = updatePlotData
        self.model = model
        layout = QVBoxLayout()
        
        
        label = QLabel(self)
        pixmap = QPixmap(self.model.imagePath)
        #pixmap = pixmap.scaledToWidth(600)
        label.setPixmap(pixmap)
        label.resize( pixmap.width(), pixmap.height())
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label,0)
        layout.addStretch()
    
        for fieldLabel,setLambda,defoultValue in model.getParametersSeters():
            
            nameLabel = QLabel()
            nameLabel.setText(fieldLabel)
            newLine = QLineEdit()
            newLine.setText(str(defoultValue))
            row = QHBoxLayout()
            row.addWidget(nameLabel)
            row.addWidget(newLine)
            
            layout.addLayout(row)
            layout.addStretch()
            self.dataColectors.append(lambda func=setLambda,field = newLine :func(field.text()))

        self.runButton = QPushButton('Uruchom')
        self.runButton.clicked.connect(lambda : self.runAction())
        
        layout.addWidget(self.runButton,0)
        layout.addStretch()

        self.setLayout(layout)

    def runAction(self):
        for dataColector in self.dataColectors:
            dataColector()
        self.updatePlotData(self.model.generateData())


class AppGUI(QWidget):
    def __init__(self,models):
        super().__init__()
        self.models = models
        self.title = 'Predator Pray'
        self.left = 10
        self.top = 10

        self.setFixedWidth(1600)
        self.setFixedHeight(800)
        self.actualSelectedModel = None
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

    def updatePlotData(self,newDataToShow):
        self._static_ax.cla()
        for label,x,y in newDataToShow:
            self._static_ax.plot(x, y, "-",label=label)
        self._static_ax.legend()
        self.canvasField.draw()


    def changeActualSelectedModel(self):
        model = self.models[ self.modelsList.currentIndex()]
      
        if self.actualSelectedModel != None:
            self.controlBox.removeWidget(self.actualSelectedModel)
            self.actualSelectedModel.deleteLater()
            self.actualSelectedModel = None
        self.actualSelectedModel = ModelControls(model, self.updatePlotData)
       
        self.controlBox.addWidget(self.actualSelectedModel)
        self.controlBox.addStretch()
       
class App:
    def __init__(self,models):
        app = QApplication(sys.argv)
        ex = AppGUI(models)
        sys.exit(app.exec_())
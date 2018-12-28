"""
Program GUI Code
uses PyQT5
"""


import sys
import qdarkstyle
import PyQt5.QtCore as cor
from PyQt5.QtCore import QDir
import PyQt5.QtGui as gui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QBoxLayout, QAction,QVBoxLayout,QHBoxLayout,QFileDialog, QFileSystemModel, QTreeView, QListView
from converter import *
import servo

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#from loader import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.lblFileName = QLabel(None,self)
        self.initUI()

    def openFileChooser(self):
        print("TODO: Open a window to choose the .zip file")

    # Function to add widgets to the main window
    def initUI(self):
        boxlayout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(boxlayout)

        lblWelcome = QLabel('Welcome to the earthquake simulation system')
        lblWelcome.setFont(gui.QFont("Verdana", 14))
        lblSubtitle = QLabel('Upload your .smc files here')
        lblSubtitle.setFont(gui.QFont("Verdana",10))

        canvas = Canvas(self, width=10,height=10)
        
        path = QDir.rootPath()

        treeview = QTreeView()
        listview = QListView()

        dirModel = QFileSystemModel()
        dirModel.setFilter(QDir.NoDotAndDotDot |  QDir.AllDirs)
        treeview.setModel(dirModel)
        
        fileModel = QFileSystemModel()
        fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
        listview.setModel(fileModel)

        treeview.setRootIndex(dirModel.index(path))
        listview.setRootIndex(fileModel.index(path))

        btnUpload = QPushButton('Upload files')
        btnUpload.setFixedSize(100, 40)
        btnUpload.setFont(gui.QFont("Verdana",10))
        btnUpload.clicked.connect(self.openFileChooser)

        btnSimulate = QPushButton('Simulate')
        btnSimulate.setFixedSize(100, 40)
        btnSimulate.setFont(gui.QFont("Verdana",10))
        btnSimulate.clicked.connect(self.simulate)  

        hbox_FileChooser = QHBoxLayout()
        hbox_FileChooser.addWidget(btnUpload);
        hbox_FileChooser.addWidget(self.lblFileName);

        vbox_treeViews = QVBoxLayout()
        vbox_treeViews.addWidget(treeview)
        vbox_treeViews.addWidget(listview)

        hbox_Graphics = QHBoxLayout()
        hbox_Graphics.addLayout(vbox_treeViews)
        hbox_Graphics.addWidget(canvas)

        boxlayout.addWidget(lblWelcome, 0, cor.Qt.AlignCenter)
        boxlayout.addWidget(lblSubtitle, 0, cor.Qt.AlignCenter)

        boxlayout.addLayout(hbox_FileChooser,0)
        boxlayout.addWidget(btnSimulate, 0, cor.Qt.AlignCenter)
        boxlayout.setAlignment(cor.Qt.AlignCenter)
        boxlayout.setSpacing(20)
        boxlayout.addLayout(hbox_Graphics,0)
    
        btnUpload = QPushButton('Upload files')
        btnUpload.setFixedSize(100, 40)
        btnUpload.setFont(gui.QFont("Verdana",10))
        btnUpload.clicked.connect(self.openFileChooser)

        self.resize(800,500)
        self.setWindowTitle('Earthquake Simulator')
        self.show()

    def openFileChooser(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName , _= QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "smc File (*.smc);;smc File (*.smc)", options=options)
        dirPath = QFileDialog.getExistingDirectory()
        update_gui(dirPath)
        self.lblFileName.setText(fileName)

    def simulate(self):
        if (self.lblFileName.text().strip()!=""):
            result=readSMCFile(self.lblFileName.text()).get('data')
            displace_accel, time = servo.receive_raw_data("COM6", 0,3600) 
            canvas.graphicCreator(displace_accel,time, self.lblFileName)
            load(result)
    
    def update_gui(self, directory):
        self.dirModel.setRootPath(directory)        

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
    
    def graphicCreator(self, displacement, time, type_move):
        '''
        Trasnform valid measurements from the movement sensor into
        two arrays to make a 2D plot
        Parameters
        -------------------
        Displacement: array
        time: array
        type_move: string tell if the movement is of displacement or acceleration
        '''
        plottie = self.figure.add_subplot(111)
        plottie.plot(time,displacement, "r-")
        plottie.title("Displacement simulation plot")
        if(type_move.find("IU.20_d")):
            plottie.title("Desplazamiento, gráfico de simulación")
            plottie.xlabel("segundos")
            plottie.ylabel("mm")
        else:
            plottie.title("Aceleración, gráfico de simulación")
            plottie.xlabel("segundos")
            plottie.ylabel("centímetros")

        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    root = Main()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
    def graphicCreator(self, displacement, time):
        '''
        Trasnform valid measurements from the movement sensor into
        two arrays to make a 2D plot
        Parameters
        -------------------
        Displacement: array
        time: array
        '''
        plottie = self.figure.add_subplot(111)
        plottie.plot(time,displacement, "r-")
        plottie.axis([1,2,3])
        plottie.set_title("Displacement simulation plot")
        self.draw()



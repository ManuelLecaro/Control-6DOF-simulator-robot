"""
Program GUI Code
uses PyQT5
"""


import sys
import PyQt5.QtCore as cor
import PyQt5.QtGui as gui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QBoxLayout, QAction

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def openFileChooser(self):
        print("TODO: Open a window to choose the .zip file")

    # Function to add widgets to the main window
    def initUI(self):
        boxlayout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(boxlayout)

        lblWelcome = QLabel('Welcome to the earthquake simulation system')
        lblWelcome.setFont(gui.QFont("Verdana", 14))
        lblSubtitle = QLabel('Download the .zip files via strongmotioncenter.org and upload them here')
        lblSubtitle.setFont(gui.QFont("Verdana",10))

        btnUpload = QPushButton('Upload files')
        btnUpload.setFixedSize(100, 40)
        btnUpload.setFont(gui.QFont("Verdana",10))
        btnUpload.clicked.connect(self.openFileChooser)


        boxlayout.addWidget(lblWelcome, 0, cor.Qt.AlignCenter)
        boxlayout.addWidget(lblSubtitle, 0, cor.Qt.AlignCenter)
        boxlayout.addWidget(btnUpload, 0, cor.Qt.AlignCenter)
        boxlayout.setAlignment(cor.Qt.AlignCenter)
        boxlayout.setSpacing(20)

        self.resize(800,500)
        self.setWindowTitle('Earthquake Simulator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Main()
    sys.exit(app.exec_())
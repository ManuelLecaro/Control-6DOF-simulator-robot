"""
Program GUI Code
uses PyQT5
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl = QLabel('Bienvenido al robot simuldor de sismos', self)

        btn = QPushButton('Subir archivos', self)
        btn.resize(btn.sizeHint())

        self.resize(800,500)
        self.setWindowTitle('Earthquake Simulator')
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Main()
    sys.exit(app.exec_())
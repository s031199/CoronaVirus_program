import sys

from PySide2.QtGui import QFont
from PySide2.QtWidgets import QGroupBox, QGridLayout, QApplication, QWidget

from Statistikalangas.Statistika_langas import *


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.groupBox = QGroupBox("Meniu")
        self.setWindowTitle("Covid-19 duomenys")
        self.setGeometry(300, 300, 500, 400)
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)
        self.setMaximumHeight(500)
        self.setMaximumWidth(400)

        self.GridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def GridLayout(self):
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        button1 = QPushButton("Statistika", self)
        gridLayout.addWidget(button1, 0, 1)
        button1.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

        button2 = QPushButton("Įšėjimas", self)
        gridLayout.addWidget(button2, 1, 1)
        button2.clicked.connect(self.exit_app)

        self.groupBox.setLayout(gridLayout)

    def exit_app(self):
        self.close()

    def on_pushButton_clicked(self):
        self.hide()
        self.dialog.show()


def main():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

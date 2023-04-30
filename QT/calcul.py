from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

from calcul_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_del.clicked.connect(self.viragenie)
        self.pushButton_num.clicked.connect(self.viragenie)
        self.pushButton_plus.clicked.connect(self.viragenie)
        self.pushButton_minus.clicked.connect(self.viragenie)
        self.pushButton_left.clicked.connect(self.viragenie)
        self.pushButton_right.clicked.connect(self.viragenie)
        self.pushButton_tokha.clicked.connect(self.viragenie)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_steret.clicked.connect(self.steret)
        self.pushButton_ravno.clicked.connect(self.ravno)

        self.pushButton_0.clicked.connect(self.viragenie)
        self.pushButton_1.clicked.connect(self.viragenie)
        self.pushButton_2.clicked.connect(self.viragenie)
        self.pushButton_3.clicked.connect(self.viragenie)
        self.pushButton_4.clicked.connect(self.viragenie)
        self.pushButton_5.clicked.connect(self.viragenie)
        self.pushButton_6.clicked.connect(self.viragenie)
        self.pushButton_7.clicked.connect(self.viragenie)
        self.pushButton_8.clicked.connect(self.viragenie)
        self.pushButton_9.clicked.connect(self.viragenie)

    def viragenie(self):
        text = self.label.text()
        self.label.setText(text + self.sender().text())

    def clear(self):
        self.label.setText('')

    def steret(self):
        text = self.label.text()
        self.label.setText(text[0:-1])

    def ravno(self):
        try:
            text = eval(str(self.label.text()))
            self.label.setText(str(text))
        except Exception:
            self.label.setText('error')

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

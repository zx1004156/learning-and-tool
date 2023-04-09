from PySide2.QtWidgets import QMainWindow

from UI import Ui_MainWindow
from UI2 import Ui_MainWindow2

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # qpushbutton doc: https://doc.qt.io/qt-5/qpushbutton.html
        self.ui.pushButton.setText('Print message!')
        self.clicked_counter = 0
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        msg = self.ui.lineEdit.text()
        self.ui.label.setText(msg)


class MainWindow_controller2(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # qpushbutton doc: https://doc.qt.io/qt-5/qpushbutton.html
        self.ui.pushButton.setText('Print message!')
        self.clicked_counter = 0
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        msg = self.ui.lineEdit.text()
        self.ui.label.setText(msg)
from PySide2.QtWidgets import QMainWindow

from UI import Ui_MainWindow

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        print('Hello')

'''
    #def buttonClicked(self):
        #msg = self.ui.lineEdit.text()
'''
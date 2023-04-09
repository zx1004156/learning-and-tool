from pyside2 import Ui_Dialog
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import *
import sys
#QWidget 可為單一視窗也可嵌入到其他視窗內
#QDialog 沒有選單欄、工具欄、狀態列，標題欄的最小化、最大化按鈕改為問號按鈕


class MainWindow(QMainWindow):#繼承至QMainWindow

    def __init__(self):
        super(MainWindow, self).__init__()#繼承QmainWindow的init
        self.ui = Ui_Dialog()#Ui_Dialog(class) 傳給 self.ui
        self.ui.setupUi(self)#setupUi底下有各種數值屬性
        self.second = Ui_Dialog()
        self.ui.pushButton.clicked.connect(lambda: self.second.show())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  #創建window物件
    window.show()#show是QmainWindow裡的方法
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

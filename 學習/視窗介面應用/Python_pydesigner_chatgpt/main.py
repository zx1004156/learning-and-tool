from PySide2.QtWidgets import QApplication, QDialog
from ui_dialog import Ui_Dialog

#繼承 QDialog 可以讓我們輕鬆地創建對話框
#繼承 Ui_Dialog 則可以讓我們使用 Qt Designer 創建的界面設計
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
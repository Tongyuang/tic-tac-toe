import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication

#import Ui_main 
import func_main

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #ui =  Ui_main.Ui_MainWindow()
        #ui.setupUi(self)
        ui = func_main.MainWindow()
        ui.setup(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestWindow()
    widget.show()
    sys.exit(app.exec())

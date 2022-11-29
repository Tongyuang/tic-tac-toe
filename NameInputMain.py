
from PyQt5.QtWidgets import QApplication,QDialog
import sys
import ui_NameInput
from PyQt5.QtCore import pyqtSignal

class NameInputMain(QDialog):
    
    _sgnal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        self.ui = ui_NameInput.Ui_QDialog()
        self.ui.setupUi(self)
        self.connection_setup()

        self._name = None
    
    def connection_setup(self):
        self.ui.pushButton.clicked.connect(self.confirm_trigger)
    
    def confirm_trigger(self):
        self._name = self.ui.textEdit.toPlainText()
        self._sgnal.emit(self._name)
        self.ui.textEdit.clear()
        self.close()
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NameInputMain()
    widget.show()
    sys.exit(app.exec())

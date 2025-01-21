import sys
import vt
import validators
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QWidget,
    QStackedLayout,
    QPushButton,
    QTabWidget,
    QToolBar,
    QStatusBar,
)
from MainWindow import Ui_MainWindow
client = vt.Client("acff4afdc1c74ab58501bb7eda32e2e66b38e6244391befefa9330c4a3661533")


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Программа для ссылок")
        self.setupUi(self)
        self.textEdit.textChanged.connect(self.validate_url)


    def validate_url(self):
        s = self.textEdit.toPlainText()
        if validators.url(s):
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
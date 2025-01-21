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
import test_rc

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
        self.pushButton.clicked.connect(self.check_url)


    def validate_url(self):
        s = self.textEdit.toPlainText()
        if validators.url(s):
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def check_url(self):
        s = self.textEdit.toPlainText()
        url_id = vt.url_id(s)
        url = client.get_object("/urls/{}", url_id)
        if url.total_votes["harmless"] > url.total_votes["malicious"]:
            self.label_2.setText("Безопасность ссылки(голоса пользователей): Безопасна")
            self.label_2.setStyleSheet("background-color:green;")
        elif url.total_votes["malicious"] > url.total_votes["harmless"]:
            self.label_2.setText("Безопасность ссылки(голоса пользователей): Опасна")
            self.label_2.setStyleSheet("background-color:red;")
        else:
            self.label_2.setText("Безопасность ссылки(голоса пользователей): Недостаточно информации")
            self.label_2.setStyleSheet("background-color:#0d6efd;")
        if url.last_analysis_stats["harmless"] > url.last_analysis_stats["malicious"] * 2 + url.last_analysis_stats["suspicious"]:
            self.label_4.setText("Безопасность ссылки(анализ): Безопасна")
            self.label_4.setStyleSheet("background-color:green;")
        elif url.last_analysis_stats["harmless"] < url.last_analysis_stats["malicious"] * 2 + url.last_analysis_stats["suspicious"]:
            self.label_4.setText("Безопасность ссылки(анализ): Опасна")
            self.label_4.setStyleSheet("background-color:red;")
        else:
            self.label_4.setText("Безопасность ссылки(анализ): Недостаточно информации")
            self.label_4.setStyleSheet("background-color:#0d6efd;")
        self.label_5.setText("Количество проверок: " + str(url.times_submitted))
        self.label_7.setText("Первая проверка: " + str(url.first_submission_date))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
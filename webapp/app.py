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
from dns_interface import get_active_interface
from dns import set_dns
from check_on_dns import check_on_dns
from sbros_dns import sbros_dns
import subprocess
import test_rc


client = vt.Client("acff4afdc1c74ab58501bb7eda32e2e66b38e6244391befefa9330c4a3661533")
paint_red = ""

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Программа для ссылок")
        self.setupUi(self)
        subprocess.run(["chcp", "65001"], shell = True)
        if check_on_dns():
            self.pushButton_3.setChecked(True)
            self.pushButton_3.setStyleSheet("background-color: green;")
            self.pushButton_3.setText("Включено")
        self.textEdit.textChanged.connect(self.validate_url)
        self.textEdit_2.textChanged.connect(self.validate_url1)
        self.pushButton.clicked.connect(self.check_url)
        self.pushButton_2.clicked.connect(self.advanced_check_url)
        self.pushButton_3.toggled.connect(self.dns_button)
        self.Set_simple.triggered.connect(self.set_simple_widget)
        self.Set_extended.triggered.connect(self.set_extended_widget)
        self.set_dns.triggered.connect(self.set_dns_widget)

    def set_simple_widget(self):
        self.stackedWidget.setCurrentIndex(0)
    def set_extended_widget(self):
        self.stackedWidget.setCurrentIndex(1)
    def set_dns_widget(self):
        self.stackedWidget.setCurrentIndex(2)
    def validate_url(self):
        s = self.textEdit.toPlainText()
        if validators.url(s):
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
    def validate_url1(self):
        s = self.textEdit_2.toPlainText()
        if validators.url(s):
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

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
        if url.last_analysis_stats["malicious"] * 2 + url.last_analysis_stats["suspicious"] < 4:
            self.label_4.setText("Безопасность ссылки(анализ): Безопасна")
            self.label_4.setStyleSheet("background-color:green;")
        elif url.last_analysis_stats["malicious"] * 2 + url.last_analysis_stats["suspicious"] > 4:
            self.label_4.setText("Безопасность ссылки(анализ): Опасна")
            self.label_4.setStyleSheet("background-color:red;")
        else:
            self.label_4.setText("Безопасность ссылки(анализ): Недостаточно информации")
            self.label_4.setStyleSheet("background-color:#0d6efd;")
        self.label_5.setText("Количество проверок: " + str(url.times_submitted))
        self.label_7.setText("Первая проверка: " + str(url.first_submission_date))

    def advanced_check_url(self):
        s = self.textEdit_2.toPlainText()
        url_id = vt.url_id(s)
        url = client.get_object("/urls/{}", url_id)
        self.label_12.setText("""Результаты анализов:
        Безопасно: %d
        Неизвестно: %d
        Подозрительно: %d
        Опасно: %d""" % (url.last_analysis_stats["harmless"], url.last_analysis_stats["undetected"], url.last_analysis_stats["suspicious"], url.last_analysis_stats["malicious"]))
        self.label_14.setText("""Голоса пользователей:
        Безопасно: %d
        Опасно: %d""" % (url.total_votes["harmless"], url.total_votes["malicious"]))
        self.label_15.setText("Дата первой проверки: " + str(url.first_submission_date))
        self.label_16.setText("Дата последней проверки: " + str(url.last_analysis_date))
        self.label_17.setText("Количество проверок: " + str(url.times_submitted))
        self.label_3.setText("Куда ведёт ссылка: " + str(url.last_final_url))
    def dns_button(self, checked):
        if checked:
            set_dns(get_active_interface())
            self.pushButton_3.setStyleSheet("background-color: green;")
            self.pushButton_3.setText("Включено")
        else:
            sbros_dns(get_active_interface())
            self.pushButton_3.setStyleSheet("background-color: red;")
            self.pushButton_3.setText("Выключено")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prefinalvesrion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  qproperty-alignment: AlignCenter;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"QPushButton {\n"
"  background-color: #0d6efd;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #0b5ed7;\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: #052F6B;\n"
"}\n"
"QPushButton:di"
                        "sabled {\n"
"  background-color: #808080;\n"
"}")
        self.Set_extended = QAction(MainWindow)
        self.Set_extended.setObjectName(u"Set_extended")
        self.Set_extended.setCheckable(True)
        self.Set_extended.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setEnabled(True)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(self.page)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verx = QVBoxLayout(self.verticalWidget)
        self.verx.setObjectName(u"verx")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verx.addItem(self.verticalSpacer)

        self.verticalWidget_2 = QWidget(self.verticalWidget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.NameLayout = QHBoxLayout(self.verticalWidget_2)
        self.NameLayout.setObjectName(u"NameLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.NameLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.verticalWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1, 1))
        self.label.setPixmap(QPixmap(u":/newPrefix/\u043f\u043b\u0430\u0448\u043a\u0430 \u0441 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\u043c.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.NameLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.NameLayout.addItem(self.horizontalSpacer)

        self.NameLayout.setStretch(0, 4)
        self.NameLayout.setStretch(1, 9)
        self.NameLayout.setStretch(2, 4)

        self.verx.addWidget(self.verticalWidget_2)

        self.textEdit = QTextEdit(self.verticalWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verx.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verx.addWidget(self.pushButton)

        self.verx.setStretch(0, 4)
        self.verx.setStretch(1, 4)
        self.verx.setStretch(2, 3)
        self.verx.setStretch(3, 1)

        self.verticalLayout_5.addWidget(self.verticalWidget)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel {\n"
"    background-color: #0d6efd;\n"
"	color:#fff;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(self.page_2)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verx_2 = QVBoxLayout(self.verticalWidget_3)
        self.verx_2.setObjectName(u"verx_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verx_2.addItem(self.verticalSpacer_2)

        self.verticalWidget_4 = QWidget(self.verticalWidget_3)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.NameLayout_2 = QHBoxLayout(self.verticalWidget_4)
        self.NameLayout_2.setObjectName(u"NameLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.NameLayout_2.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.verticalWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(1, 1))
        self.label_11.setPixmap(QPixmap(u":/newPrefix/\u043f\u043b\u0430\u0448\u043a\u0430 \u0441 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\u043c.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.NameLayout_2.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.NameLayout_2.addItem(self.horizontalSpacer_4)

        self.NameLayout_2.setStretch(0, 4)
        self.NameLayout_2.setStretch(1, 9)
        self.NameLayout_2.setStretch(2, 4)

        self.verx_2.addWidget(self.verticalWidget_4)

        self.textEdit_2 = QTextEdit(self.verticalWidget_3)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verx_2.addWidget(self.textEdit_2)

        self.pushButton_2 = QPushButton(self.verticalWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verx_2.addWidget(self.pushButton_2)

        self.verx_2.setStretch(0, 4)
        self.verx_2.setStretch(1, 4)
        self.verx_2.setStretch(2, 3)
        self.verx_2.setStretch(3, 1)

        self.verticalLayout_9.addWidget(self.verticalWidget_3)

        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QLabel {\n"
"    background-color: #0d6efd;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_7)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_7.addWidget(self.label_17)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_8 = QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_8.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_8)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20)


        self.horizontalLayout_2.addWidget(self.widget_8)


        self.verticalLayout_9.addWidget(self.widget_5)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.Set_extended)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Set_extended.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c", None))
#if QT_CONFIG(tooltip)
        self.Set_extended.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0430\u0435\u0442 \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0421\u0441\u044b\u043b\u043a\u0443", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438(\u0430\u043d\u0430\u043b\u0438\u0437):</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438(\u0433\u043e\u043b\u043e\u0441\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439):</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u043a:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u041f\u0435\u0440\u0432\u0430\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430:</span></p></body></html>", None))
        self.label_11.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0421\u0441\u044b\u043b\u043a\u0443", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


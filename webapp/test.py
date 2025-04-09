
from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve
import sys


class StackedWidgetAnimation(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    def setCurrentIndex(self, index):
        # Get current and next widget geometry
        current_widget = self.currentWidget()
        next_widget = self.widget(index)

        if current_widget and next_widget:
            current_geom = current_widget.geometry()
            next_geom = next_widget.geometry()

            # Set up animation for sliding effect
            self.animation.setStartValue(current_geom)
            self.animation.setEndValue(next_geom)
            self.animation.start()

        super().setCurrentIndex(index)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Create stacked widget with animation
        self.stacked_widget = StackedWidgetAnimation()

        # Add pages to stacked widget
        page1 = QWidget()
        page1.setStyleSheet("background-color: red;")
        self.stacked_widget.addWidget(page1)

        page2 = QWidget()
        page2.setStyleSheet("background-color: green;")
        self.stacked_widget.addWidget(page2)

        page3 = QWidget()
        page3.setStyleSheet("background-color: blue;")
        self.stacked_widget.addWidget(page3)

        # Add buttons to switch pages
        btn1 = QPushButton("Page 1")
        btn1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(btn1)

        btn2 = QPushButton("Page 2")
        btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(btn2)

        btn3 = QPushButton("Page 3")
        btn3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(btn3)

        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())

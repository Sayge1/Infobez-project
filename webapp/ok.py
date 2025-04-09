import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                               QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel)
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QParallelAnimationGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animated Stacked Widget")
        self.setGeometry(100, 100, 400, 300)

        # Главный контейнер с вертикальной компоновкой
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Создаем QStackedWidget и добавляем страницы
        self.stacked_widget = QStackedWidget()

        # Страница 1
        page1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Страница 1"))
        page1.setLayout(layout1)

        # Страница 2
        page2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Страница 2"))
        page2.setLayout(layout2)

        self.stacked_widget.addWidget(page1)
        self.stacked_widget.addWidget(page2)

        # Панель с кнопками
        button_layout = QHBoxLayout()

        self.btn_prev = QPushButton("Назад")
        self.btn_prev.clicked.connect(lambda: self.slide_to_index(0))
        button_layout.addWidget(self.btn_prev)

        self.btn_next = QPushButton("Вперед")
        self.btn_next.clicked.connect(lambda: self.slide_to_index(1))
        button_layout.addWidget(self.btn_next)

        # Добавляем все в главный layout
        main_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(button_layout)

        self.setCentralWidget(main_widget)

    def slide_to_index(self, new_index):
        current_index = self.stacked_widget.currentIndex()
        if current_index == new_index:
            return

        # Определение направления анимации
        direction = "left" if new_index > current_index else "right"

        # Получаем текущий и следующий виджеты
        current_widget = self.stacked_widget.widget(current_index)
        next_widget = self.stacked_widget.widget(new_index)

        # Создаем снимки виджетов
        current_pixmap = current_widget.grab()
        next_pixmap = next_widget.grab()

        # Создаем метки для анимации
        self.current_label = QLabel(self)
        self.current_label.setPixmap(current_pixmap)
        self.current_label.setGeometry(self.stacked_widget.geometry())

        self.next_label = QLabel(self)
        self.next_label.setPixmap(next_pixmap)
        self.next_label.setGeometry(self.stacked_widget.geometry())

        # Устанавливаем начальные позиции
        if direction == "left":
            self.next_label.move(self.stacked_widget.width(), 0)
        else:
            self.next_label.move(-self.stacked_widget.width(), 0)

        self.current_label.show()
        self.next_label.show()

        # Группа анимаций для параллельного выполнения
        self.anim_group = QParallelAnimationGroup()

        # Анимация для текущей метки
        anim_current = QPropertyAnimation(self.current_label, b"pos")
        anim_current.setDuration(500)
        anim_current.setEasingCurve(QEasingCurve.OutCubic)
        start_pos_current = self.current_label.pos()
        end_pos_current = QPoint(-self.stacked_widget.width(), 0) if direction == "left" else QPoint(
            self.stacked_widget.width(), 0)
        anim_current.setStartValue(start_pos_current)
        anim_current.setEndValue(end_pos_current)

        # Анимация для следующей метки
        anim_next = QPropertyAnimation(self.next_label, b"pos")
        anim_next.setDuration(500)
        anim_next.setEasingCurve(QEasingCurve.OutCubic)
        start_pos_next = self.next_label.pos()
        anim_next.setStartValue(start_pos_next)
        anim_next.setEndValue(QPoint(0, 0))

        self.anim_group.addAnimation(anim_current)
        self.anim_group.addAnimation(anim_next)

        # По завершении анимации обновляем индекс и скрываем метки
        self.anim_group.finished.connect(
            lambda: self.on_animation_finished(new_index)
        )
        self.anim_group.start()

    def on_animation_finished(self, new_index):
        self.stacked_widget.setCurrentIndex(new_index)
        self.current_label.deleteLater()
        self.next_label.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
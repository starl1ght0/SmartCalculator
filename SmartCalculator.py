from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QVBoxLayout, QDateEdit, QGridLayout, QPushButton,
                             QLineEdit, QFormLayout)
from PyQt5.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)
        # first page
        personal_page = QWidget(self)
        layout = QFormLayout()
        personal_page.setLayout(layout)
        personal_page.setFixedSize(100, 20)
        # second page
        contact_page = QWidget(self)
        layout = QFormLayout()
        contact_page.setLayout(layout)
        contact_page.setFixedSize(100, 20)
        tab.addTab(personal_page, 'Personal Info')
        tab.addTab(contact_page, 'Contact Info')
        tab.resize(0, 0)
        self.show()

    def initUI(self):
        grid = QGridLayout()  # Создание сетки grid
        self.setLayout(grid)  # Для объекта self устанавливает сетку grid в качестве основного макета

        self.display = QLineEdit()  # Создаем дисплей для отображения наших вычислений
        self.display.setFont(QFont('jetbrains mono', 20))  # устанавливаем для дисплея шрифт и размер
        self.display.setFixedSize(407, 50)  # Размер дисплея
        grid.addWidget(self.display, 0, 0, 1, 0)  # добавляем дисплей на сетку grid корд.(Лево,право,вниз,вверх)
        # Создаем кнопочки :3
        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            '0', '.', '+', '='
        ]

        row_val = 1  # переменные для отслеживания координат кнопочек в сетке grid
        col_val = 0

        for button in buttons:  # Логика для '=' в кнопках
            if button == '=':
                btn = QPushButton(button)  # Создаем кнопку btn
                btn.clicked.connect(self.calculate)  # При нажатии вызывается функция calculate. Метод connect - связь
                btn.setFixedSize(90, 50)  # Размер кнопки '='
                btn.setFont(QFont('jetbrains mono', 16))  # Шрифт текста кнопки
                btn.setStyleSheet('background-color: #6e4949; color: #fff')  # цвета кнопки
                grid.addWidget(btn, row_val, col_val, 1, 4)  # размещение кнопки на сетке grid
                row_val += 1
            else:
                btn = QPushButton(button)
                btn.clicked.connect(self.append_text)
                btn.setFixedSize(90, 50)
                btn.setFont(QFont('jetbrains mono', 16))
                grid.addWidget(btn, row_val, col_val)
                col_val += 1
                if col_val > 3:
                    col_val = 0
                    row_val += 1

        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear_display)
        self.clear_button.setFixedSize(410, 50)
        self.clear_button.setFont(QFont('jetbrains mono', 16))
        self.clear_button.setStyleSheet('background-color: #ff7f7f; color: #ffffff')
        grid.addWidget(self.clear_button, row_val, 0, 1, 4)

        # Кнопочка close
        self.close_button = QPushButton('Close')  # Создание кнопки
        self.close_button.clicked.connect(self.close_window)  # При нажатии передаётся функция закрытия окна
        self.close_button.setFixedSize(410, 50)
        self.close_button.setFont(QFont('jetbrains mono', 16))  # Шрифт текста кнопки
        grid.addWidget(self.close_button, row_val + 1, 0, 1, 4)

        self.setWindowTitle('Ingiborg The Calculator')
        self.setGeometry(550, 200, 560, 768)

        grid.setContentsMargins(200, 100, 200, 200)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(20)

    def append_text(self):
        button = self.sender()
        text = button.text()
        if self.display.text() == 'Error':
            self.display.setText('')
        self.display.setText(self.display.text() + text)

    def calculate(self):
        try:
            result = eval(self.display.text())
            if result % 1 == 0:
                self.display.setText(str(int(result)))
            else:
                self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')

    def clear_display(self):
        self.display.setText('')

    def close_window(self):  # Функция закрытия окна
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    window = Calculator()
    window.setStyleSheet('background-color: #fce2e2;')  # Цвет фона окна
    window.show()  # Окно по умолчанию скрыто, делаем его видным
    sys.exit(app.exec_())  # Программа всегда завершается корректно

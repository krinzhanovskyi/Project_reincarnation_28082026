from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class PocketWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Делаем окно без рамок и заставляем висеть поверх всех остальных окон
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        
        # Разрешаем прозрачность фона
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Базовый стиль окна: полупрозрачный темный фон и скругленные углы
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(30, 30, 30, 230);
                border-radius: 15px;
                border: 1px solid #555;
            }
        """)

        # Добавляем временный текст внутрь окна
        layout = QVBoxLayout()
        self.label = QLabel("Содержимое папки будет здесь...", self)
        self.label.setStyleSheet("color: white; font-size: 14px; background: transparent; border: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(self.label)
        self.setLayout(layout)

    def show_at(self, x, y):
        # Сдвигаем окно немного вправо и вниз от курсора, чтобы оно не перекрывало саму папку
        self.move(int(x) + 20, int(y) + 20)
        self.show()

    def hide_window(self):
        self.hide()
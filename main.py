import sys
from PyQt6.QtWidgets import QApplication
from backend.mouse_tracker import MouseTracker
from ui.pocket_window import PocketWindow
from backend.win_api import get_desktop_folder_under_cursor  # <-- Новый импорт

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False) 
    
    pocket = PocketWindow()
    tracker = MouseTracker()
    
    # Теперь трекер вызывает нашу проверку, а не окно напрямую
    def handle_hover(x, y):
        # Спрашиваем Windows, есть ли тут папка на рабочем столе
        folder_path = get_desktop_folder_under_cursor(x, y)
        
        if folder_path:
            print(f"[*] Найдена папка: {folder_path}")
            # Пока просто открываем окно, в будущем передадим туда файлы
            pocket.show_at(x, y)
        else:
            # Если папки нет (пустое место или другая программа), окно не появится
            pass

    tracker.hover.connect(handle_hover)
    tracker.move.connect(pocket.hide_window)
    
    print("Запуск Project Reincarnation...")
    print("Теперь виджет появится ТОЛЬКО над папками на рабочем столе.")
    
    tracker.start()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
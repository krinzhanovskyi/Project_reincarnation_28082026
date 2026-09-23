import time
from PyQt6.QtCore import QObject, QTimer, pyqtSignal
from PyQt6.QtGui import QCursor
from config import HOVER_DELAY

class MouseTracker(QObject):
    hover = pyqtSignal(int, int)
    move = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.last_pos = (0, 0)
        self.last_time = time.time()
        self.is_hovering = False
        self.timer = QTimer()
        self.timer.timeout.connect(self._check_mouse)
        
    def start(self):
        self.last_time = time.time()
        self.timer.start(50)

    def stop(self):
        self.timer.stop()

    def _check_mouse(self):
        pos = QCursor.pos()
        current_pos = (pos.x(), pos.y())
        
        if current_pos != self.last_pos:
            self.last_pos = current_pos
            self.last_time = time.time()
            
            if self.is_hovering:
                self.is_hovering = False
                self.move.emit()
        else:
            if not self.is_hovering and (time.time() - self.last_time) >= HOVER_DELAY:
                self.is_hovering = True
                self.hover.emit(current_pos[0], current_pos[1])
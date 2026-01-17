from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self._pixmap: QPixmap | None = None

    def show_image(self, path: str):
        self._pixmap = QPixmap(path)
        self._update_pixmap()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_pixmap()

    def _update_pixmap(self):
        if not self._pixmap or self._pixmap.isNull():
            return

        scaled = self._pixmap.scaled(
            self.label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.label.setPixmap(scaled)


from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)

        # Image
        self.label = QLabel(alignment=Qt.AlignCenter)
        root.addWidget(self.label, stretch=1)

        # Overlay bar
        overlay = QHBoxLayout()
        overlay.setSpacing(48)

        left = QLabel("←  Delete\n🗑")
        right = QLabel("Keep  →\n✔")

        for lbl in (left, right):
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("""
                color: #aaa;
                font-size: 18px;
            """)

        overlay.addWidget(left, alignment=Qt.AlignLeft)
        overlay.addStretch()
        overlay.addWidget(right, alignment=Qt.AlignRight)

        root.addLayout(overlay)

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

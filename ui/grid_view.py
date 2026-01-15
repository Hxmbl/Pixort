from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class ImageGridView(QWidget):
    """
    Scrollable grid of image thumbnails.
    This view is read-only; it does NOT know about keep/delete state.
    """

    def __init__(self, image_paths: list[str], thumb_size: int = 160):
        super().__init__()

        self.image_paths = image_paths
        self.thumb_size = thumb_size

        self._build_ui()

    def _build_ui(self):
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        outer_layout.addWidget(scroll)

        container = QWidget()
        scroll.setWidget(container)

        self.grid = QGridLayout(container)
        self.grid.setSpacing(12)
        self.grid.setContentsMargins(12, 12, 12, 12)

        self._populate_grid()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        outer_layout.addWidget(self.scroll)

        container = QWidget()
        self.scroll.setWidget(container)

    def scroll_to_bottom_right(self):
        bar_v = self.scroll.verticalScrollBar()
        bar_h = self.scroll.horizontalScrollBar()

        bar_v.setValue(bar_v.maximum())
        bar_h.setValue(bar_h.maximum())


    def _populate_grid(self):
        if not self.image_paths:
            return

        columns = 5
        row = 0
        col = 0

        # Start bottom-right visually by filling top-left first
        # then scrolling to bottom later
        for path in self.image_paths:
            label = QLabel()
            label.setFixedSize(QSize(self.thumb_size, self.thumb_size))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("background-color: #111; border: 1px solid #333;")

            pixmap = QPixmap(path)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(
                    self.thumb_size,
                    self.thumb_size,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
                label.setPixmap(pixmap)

            self.grid.addWidget(label, row, col)

            col += 1
            if col >= columns:
                col = 0
                row += 1
